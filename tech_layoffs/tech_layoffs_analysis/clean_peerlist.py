import pandas as pd
import re
import time
from geopy.geocoders import Nominatim
from typing import Tuple
from functools import lru_cache

# --- Configuration & Mappings ---

INPUT_FILE = "tech_layoffs_csv/peerlist.csv"
OUTPUT_FILE = "tech_layoffs_csv/peerlist_cleaned.csv"

COUNTRY_MAPPING = {
    "IN": "India", "US": "USA", "NL": "Netherlands", "CN": "China", 
    "IL": "Israel", "GB": "UK", "SE": "Sweden", "CA": "Canada", 
    "AU": "Australia", "JP": "Japan", "BR": "Brazil", "FI": "Finland", 
    "SG": "Singapore", "FR": "France", "CY": "Cyprus", "IE": "Ireland", 
    "NO": "Norway", "DE": "Germany", "LT": "Lithuania", "KE": "Kenya"
}

CONTINENT_MAPPING = {
    "India": "Asia", "China": "Asia", "Israel": "Asia", "Japan": "Asia", "Singapore": "Asia",
    "USA": "North America", "Canada": "North America",
    "Netherlands": "Europe", "UK": "Europe", "Sweden": "Europe", "Finland": "Europe", 
    "France": "Europe", "Cyprus": "Europe", "Ireland": "Europe", "Norway": "Europe", 
    "Germany": "Europe", "Lithuania": "Europe",
    "Australia": "Oceana",
    "Brazil": "South America",
    "Kenya": "Africa"
}

SF_BAY_AREA = {
    "San Francisco", "Palo Alto", "Mountain View", "Menlo Park", "Sunnyvale", 
    "San Bruno", "San Jose", "Redwood City", "Alameda", "San Mateo", 
    "Oakland", "Santa Clara", "Fremont", "Walnut Creek", "Foster City", 
    "Berkeley", "Burlingame", "Newark", "Pleasanton", "San Carlos"
}

CASCADIA = {"Vancouver", "Seattle", "Portland", "Bellevue", "Redmond", "Kirkland"}

# Mapping for USState column (States for USA, 'non' or province for others)
# tech_layoffs_til_2025.csv uses specific state names for USA and 'non' for others (or province name in some cases)
STATE_PROVINCE_MAPPING = {
    "Seattle": "Washington", "San Francisco": "California", "Bengaluru": "Karnataka",
    "Vancouver": "British Columbia", "New York": "New York", "Tel Aviv-Yafo": "non",
    "Gurugram": "Haryana", "Toronto": "Ontario", "Austin": "Texas", "Sydney": "New South Wales",
    "Noida": "Uttar Pradesh", "Mumbai": "Maharashtra", "Montreal": "Quebec",
    "Palo Alto": "California", "Menlo Park": "California", "San Jose": "California",
    "London": "England", "Stockholm": "non", "Herzliya": "non", "Amsterdam": "non",
    "Santa Monica": "California", "Redwood City": "California", "Newark": "California",
    "Sunnyvale": "California", "Oklahoma City": "Oklahoma", "Oakland": "California",
    "Washington": "District of Columbia", "Denver": "Colorado", "Bellevue": "Washington",
    "Columbus": "Ohio", "Milwaukee": "Wisconsin", "Cary": "North Carolina",
    "Waterloo": "Ontario", "Singapore": "non", "Paris": "non", "Bozeman": "Montana",
    "West Hollywood": "California", "Farnborough": "non", "Brisbane": "Queensland",
    "Melbourne": "Victoria", "Brooklyn": "New York", "Burlington": "Massachusetts",
    "Chicago": "Illinois", "Los Gatos": "California", "Hatfield": "non", "Hatfield, GB": "non",
    "Israel": "non", "Qualicum Beach": "British Columbia", "Espoo": "non",
    "Bastrop": "Texas", "Waterloo, CA": "Ontario", "Stockholm, SE": "non",
    "Sydney, AU": "New South Wales", "San Jose, US": "California",
    "New York, US": "New York", "Seattle, US": "Washington", "San Francisco, US": "California"
}

# --- Helper Functions ---

geolocator = Nominatim(user_agent="tech_layoffs_cleaner")

@lru_cache(maxsize=None)
def get_coordinates(city: str, country: str) -> Tuple[float, float]:
    """Get coordinates for a city and country."""
    query = f"{city}, {country}" if city and country else (city or country)
    try:
        location = geolocator.geocode(query)
        if location:
            return location.latitude, location.longitude
    except Exception as e:
        print(f"Error geocoding {query}: {e}")
    return None, None

def parse_truncate(value: str) -> Tuple[float, float]:
    """Extract Laid_Off and Percentage from the 'truncate' string."""
    if pd.isna(value) or value == "":
        return None, None
    
    laid_off = None
    percentage = None
    
    # Extract laid off count (numeric before optional parenthesis)
    count_match = re.search(r'^(\d+)', str(value))
    if count_match:
        laid_off = float(count_match.group(1))
    
    # Extract percentage (numeric inside parenthesis)
    perc_match = re.search(r'\((\d+)%\)', str(value))
    if perc_match:
        percentage = float(perc_match.group(1))
        
    return laid_off, percentage

# --- Main Script ---

def main():
    print(f"Reading {INPUT_FILE}...")
    df_raw = pd.read_csv(INPUT_FILE)
    
    cleaned_data = []
    
    for i, row in df_raw.iterrows():
        # 1. Basic Company & Industry
        company = row['company']
        industry = row['Industry']
        
        # 2. Parse Truncate column
        laid_off, percentage = parse_truncate(row['truncate'])
        
        # 3. Parse Date & Year
        try:
            date_obj = pd.to_datetime(row['layoff date'])
            date_str = date_obj.strftime("%Y-%m-%d")
            year = date_obj.year
        except:
            date_str = None
            year = None
            
        # 4. Parse Location
        loc_parts = [p.strip() for p in str(row['location']).split(',')]
        if len(loc_parts) >= 2:
            city = loc_parts[0]
            country_code = loc_parts[1]
        else:
            city = loc_parts[0]
            country_code = city # Fallback for cases like "Sweden" or "France"
            
        country = COUNTRY_MAPPING.get(country_code, country_code)
        continent = CONTINENT_MAPPING.get(country, "Unknown")
        
        # 5. Determine Region
        if city in SF_BAY_AREA:
            region = "San Francisco Bay Area"
        elif city in CASCADIA:
            region = "Cascadia"
        else:
            region = "other"
            
        # 6. Determine USState (State/Province)
        us_state = STATE_PROVINCE_MAPPING.get(city, "non")
        
        # 7. Coordinates (Fetch with sleep to respect API limits)
        print(f"[{i+1}/{len(df_raw)}] Geocoding {city}, {country}...")
        lat, lon = get_coordinates(city, country)
        time.sleep(1) # Nominatim policy: max 1 request per second
        
        # 8. Company Size Calculations
        size_before = None
        size_after = None
        if laid_off and percentage and percentage > 0:
            size_before = round(laid_off / (percentage / 100))
            size_after = size_before - laid_off

        # Assemble row in tech_layoffs_til_2025.csv format
        cleaned_data.append({
            "Nr": i + 1,
            "Company": company,
            "Location_HQ": city,
            "Region": region,
            "USState": us_state,
            "Country": country,
            "Continent": continent,
            "Laid_Off": laid_off,
            "Date_layoffs": date_str,
            "Percentage": percentage,
            "Company_Size_before_Layoffs": size_before,
            "Company_Size_after_layoffs": size_after,
            "Industry": industry,
            "Stage": "Unknown",
            "Money_Raised_in__mil": None,
            "Year": year,
            "latitude": lat,
            "longitude": lon
        })
        
    df_cleaned = pd.DataFrame(cleaned_data)
    
    # Ensure correct column order
    cols = ["Nr", "Company", "Location_HQ", "Region", "USState", "Country", 
            "Continent", "Laid_Off", "Date_layoffs", "Percentage", 
            "Company_Size_before_Layoffs", "Company_Size_after_layoffs", 
            "Industry", "Stage", "Money_Raised_in__mil", "Year", "latitude", "longitude"]
    df_cleaned = df_cleaned[cols]
    
    print(f"Saving cleaned data to {OUTPUT_FILE}...")
    df_cleaned.to_csv(OUTPUT_FILE, index=False)
    print("Done!")

if __name__ == "__main__":
    main()
