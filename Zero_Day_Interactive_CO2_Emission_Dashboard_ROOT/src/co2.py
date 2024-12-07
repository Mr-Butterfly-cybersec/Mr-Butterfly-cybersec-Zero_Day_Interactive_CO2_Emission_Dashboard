import pandas as pd
import matplotlib.pyplot as plt 


print("\nCO2 emission comparision between countries")

raw_df = pd.read_csv('energy.csv')
column_filtered = raw_df[['Country', 'Energy_type','Year', 'CO2_emission']]
country1 = input("Country 1: ")
country2 = input("Country 2: ")
df_country1 = column_filtered.loc[(column_filtered['Country'] == country1) & (column_filtered['Energy_type'] == 'all_energy_types')]
df_country2 = column_filtered.loc[(column_filtered['Country'] == country2) & (column_filtered['Energy_type'] == 'all_energy_types')]

x1 = df_country1.get('Year').tolist()
y1 = df_country1.get('CO2_emission').tolist()
plt.plot(x1, y1, label=country1)

x1 = df_country2.get('Year').tolist()
y1 = df_country2.get('CO2_emission').tolist()
plt.plot(x1, y1, label=country2)

plt.xlabel('Years')
plt.ylabel('CO2 emission')
plt.title(f"CO2 emission comparison between {country1} and {country2}")

plt.legend()
plt.show()
