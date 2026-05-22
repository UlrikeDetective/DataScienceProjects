import pandas as pd
import numpy as np

# --- Configuration ---

MAIN_FILE = "tech_layoffs_csv/tech_layoffs_til_2025.csv"
PEERLIST_FILE = "tech_layoffs_csv/peerlist_cleaned.csv"
MERGED_FILE = "tech_layoffs_csv/tech_layoffs_til_2026.csv"

# Summary files to update
COUNTRY_SUM_FILE = "tech_layoffs_csv/layoffs_country_sum.csv"
CONTINENT_SUM_FILE = "tech_layoffs_csv/layoffs_continent_sum.csv"
COUNTRY_YEAR_SUM_FILE = "tech_layoffs_csv/layoffs_Country_sum_year.csv"
CONTINENT_YEAR_SUM_FILE = "tech_layoffs_csv/layoffs_Continent_sum_year.csv"

def main():
    print("Loading datasets...")
    df_main = pd.read_csv(MAIN_FILE)
    df_peerlist = pd.read_csv(PEERLIST_FILE)
    
    # 1. Merge datasets
    print(f"Merging {len(df_main)} rows from main and {len(df_peerlist)} rows from peerlist...")
    df_merged = pd.concat([df_main, df_peerlist], ignore_index=True)
    
    # 2. Re-index the 'Nr' column
    df_merged['Nr'] = range(1, len(df_merged) + 1)
    
    # 3. Sort by Date_layoffs (optional but good for consistency)
    df_merged['Date_layoffs'] = pd.to_datetime(df_merged['Date_layoffs'])
    df_merged = df_merged.sort_values(by='Date_layoffs', ascending=True)
    
    # Re-re-index Nr after sorting to keep chronological order sequential
    df_merged['Nr'] = range(1, len(df_merged) + 1)
    
    # Save merged file
    print(f"Saving merged dataset to {MERGED_FILE}...")
    df_merged.to_csv(MERGED_FILE, index=False)
    
    # 4. Generate Summaries
    print("Generating updated summaries...")
    
    # Filter for rows with layoffs count
    df_with_layoffs = df_merged.dropna(subset=['Laid_Off'])
    
    # Country Summary
    country_sum = df_with_layoffs.groupby('Country')['Laid_Off'].sum().reset_index()
    country_sum.columns = ['Country', 'Total_Laid_off']
    country_sum = country_sum.sort_values(by='Country')
    country_sum.to_csv(COUNTRY_SUM_FILE, index=False)
    print(f"Updated {COUNTRY_SUM_FILE}")
    
    # Continent Summary
    continent_sum = df_with_layoffs.groupby('Continent')['Laid_Off'].sum().reset_index()
    continent_sum.columns = ['Continent', 'Total_Laid_off']
    continent_sum = continent_sum.sort_values(by='Continent')
    continent_sum.to_csv(CONTINENT_SUM_FILE, index=False)
    print(f"Updated {CONTINENT_SUM_FILE}")
    
    # Country + Year Summary
    # Pivot table for Country vs Year
    country_year_pivot = df_with_layoffs.pivot_table(
        index='Country', 
        columns='Year', 
        values='Laid_Off', 
        aggfunc='sum', 
        fill_value=0
    )
    # Add Total column
    country_year_pivot['Total_Laid_off'] = country_year_pivot.sum(axis=1)
    country_year_pivot = country_year_pivot.reset_index()
    country_year_pivot.to_csv(COUNTRY_YEAR_SUM_FILE, index=False)
    print(f"Updated {COUNTRY_YEAR_SUM_FILE}")

    # Continent + Year Summary
    continent_year_pivot = df_with_layoffs.pivot_table(
        index='Continent', 
        columns='Year', 
        values='Laid_Off', 
        aggfunc='sum', 
        fill_value=0
    )
    continent_year_pivot['Total_Laid_off'] = continent_year_pivot.sum(axis=1)
    continent_year_pivot = continent_year_pivot.reset_index()
    continent_year_pivot.to_csv(CONTINENT_YEAR_SUM_FILE, index=False)
    print(f"Updated {CONTINENT_YEAR_SUM_FILE}")
    
    print("Integration complete!")


if __name__ == "__main__":
    main()
