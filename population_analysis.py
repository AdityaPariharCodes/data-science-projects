import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'country': ['China', 'India', 'USA', 'Indonesia', 'Brazil', 
                'Pakistan', 'Nigeria', 'Bangladesh', 'Russia', 'Ethiopia'],

    'continent': ['Asia', 'Asia', 'North America', 'Asia', 'South America',
                  'Asia', 'Africa', 'Asia', 'Europe', 'Africa'],

    'population_2023': [1425671352, 1428627663, 339996563,
                        277534122, 216422446, 231402117,
                        223804632, 172954319, 144444359, 126527060],

    'gdp_per_capita': [12541, 2389, 63544, 4357, 9673,
                       1505, 2065, 2688, 12575, 925]
}

df = pd.DataFrame(data)
print("--- Shape ---")
print(df.shape)
print("--- info ---")
print(df.info())
print("--- describe ---")
print(df.describe())

pop = df['population_2023'].to_numpy()

total = np.sum(pop)
average = np.mean(pop)
largest = np.max(pop)
smallest = np.min(pop)
spread = np.ptp(pop)

print(f"Total: {total:,}")
print(f"Average:{average:,.0f}")
print(f"Largest:{largest:,}")
print(f"Smallest:{smallest:,}")
print(f"Spread:{spread:,.0f}")

print("--- Countries with population above 300 million ---")
big = df[df['population_2023']>300_000_000]
print(big[['country', 'population_2023']])

print("--- sorted largest to smallest ---")
sorted_df = df.sort_values('population_2023', ascending=False)
print(sorted_df[['country', 'population_2023']])

print("--- Total Population per Continent ---")
by_continent = df.groupby('continent')['population_2023'].sum()
print(by_continent.sort_values(ascending=False))

print("--- average GDP per Continent ---")
avg_gdp = df.groupby('continent')['gdp_per_capita'].mean()
print(avg_gdp.round(0))

sorted_df = df.sort_values('population_2023')
plt.figure(figsize=(10,6))
plt.barh(sorted_df['country'],
         sorted_df['population_2023'] / 1_000_000)

plt.xlabel('population (millions)')
plt.title('Top 10 most populous countries (2023)')
plt.tight_layout()
plt.savefig('population_bar.png')
plt.show()

plt.figure(figsize=(10, 7))
for _, row in df.iterrows():
    plt.scatter(row['population_2023'] / 1_000_000,
                row['gdp_per_capita'],
                s=80,color='steelblue')
    
plt.xlabel('population (millions)')
plt.ylabel('GDP per capita (USD)')
plt.title('population vs wealth: top 10 countries')
plt.tight_layout()
plt.savefig('scatter.png')
plt.show()