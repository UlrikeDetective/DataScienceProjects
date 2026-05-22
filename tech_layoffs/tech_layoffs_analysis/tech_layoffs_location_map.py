import pandas as pd

# Load the new 2026 dataset
df = pd.read_csv('tech_layoffs_csv/tech_layoffs_til_2026.csv', delimiter=',')

# Display the first few rows of the DataFrame
print(df.head())

# Display the DataFrame information
df.info(verbose=True)

# Latitude and longitude are already floats in the new dataset, but ensuring consistency
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

import folium
from branca.element import Figure

# Create a Figure object
fig = Figure(width=1024, height=600)

# Create a Folium Map object covering the whole world
fmap = folium.Map(location=[20, 0], tiles="openstreetmap", zoom_start=2)

# Filter out rows with NaN latitude or longitude
df_filtered = df.dropna(subset=['latitude', 'longitude'])

# Define the path to the custom icon
icon_path = 'tech_layoffs_pictures/redsmallpin.png' 

# Iterate over each row in the filtered DataFrame (using a subset to avoid map clutter if needed, or all)
for index, row in df_filtered.iterrows():
    latitude, longitude = row['latitude'], row['longitude']
    name = f"{row['Company']} ({row['Location_HQ']})" 
    
    # Create a custom icon
    try:
        icon = folium.CustomIcon(icon_image=icon_path, icon_size=(20, 20)) 
        folium.Marker(location=[latitude, longitude], popup=name, icon=icon).add_to(fmap)
    except:
        folium.Marker(location=[latitude, longitude], popup=name).add_to(fmap)

# Add the Folium Map object to the Figure
fig.add_child(fmap)

import plotly.express as px

# 1. World Treemap of Layoffs
fig_world = px.treemap(df_filtered, 
                       path=['Continent', 'Country', 'Industry'], 
                       values='Laid_Off',
                       color='Continent',
                       title='Global Layoffs Treemap')
fig_world.show()

# 2. USA specific treemap
usa_df = df_filtered[df_filtered['Country'] == 'USA']
fig_usa = px.treemap(usa_df, 
                     path=['USState', 'Location_HQ', 'Company'], 
                     values='Laid_Off',
                     color='USState',
                     title='USA Layoffs Distribution')
fig_usa.show()

# 3. SF Bay Area specific treemap
sf_df = df_filtered[df_filtered['Region'] == 'San Francisco Bay Area']
fig_sf = px.treemap(sf_df, 
                    path=['Location_HQ', 'Company'], 
                    values='Laid_Off',
                    color='Location_HQ',
                    title='San Francisco Bay Area Layoffs')
fig_sf.show()

