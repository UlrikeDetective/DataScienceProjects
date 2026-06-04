import pandas as pd

file_path = 'tech_layoffs_csv/tech_layoffs_til_2026.csv'
df = pd.read_csv(file_path)

mapping = {
    'UK': 'United Kingdom',
    'USA': 'United States',
    'United Arabian Emirates': 'United Arab Emirates',
    'Uruquay': 'Uruguay'
}

df['Country'] = df['Country'].replace(mapping)
df.to_csv(file_path, index=False)
print('Cleanup complete.')
