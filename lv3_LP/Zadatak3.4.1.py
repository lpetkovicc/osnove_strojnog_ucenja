import pandas as pd
import numpy as np 

data = pd.read_csv('data_C02_emission.csv')

# Zadatak pod a
length = len(data['Make'])
print(f'DataFrame ima {length} mjerenja')

for col in data.columns:
    print(f"{col} has a type of {data[col].dtype}")

data['Vehicle Class'] = data['Vehicle Class'].astype('category')

print(f"Redovi s izostalim vrijednostima: {data.isnull().sum()}")
print(f"Duplicirane vrijednosti: {data.duplicated().sum()}")



# Zadatak pod b
least_consuming = data.nsmallest(3, 'Fuel Consumption City (L/100km)')
most_consuming = data.nlargest(3, 'Fuel Consumption City (L/100km)')

print('Most consuming: ')
print(most_consuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])
print('Least consuming: ')
print(least_consuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])



# Zadatak pod c
selected_data = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
length = len(selected_data['Make'])
print(f"Postoji {length} vozila koje imaju motor izmedu 2.5 i 3.5 L")

print(f"Prosjecni C02 ovih vozila jest: {selected_data['CO2 Emissions (g/km)'].mean()} g/km")


# Zadatak pod d
selected_data = data[(data['Make'] == 'Audi')]
length = len(selected_data['Make'])
print(f"U mjerenjima ima {length} mjerenja koja se odnose na marku Audi")

selected_data = selected_data[(selected_data['Cylinders'] == 4)]
print(f"Prosjecni CO2 4 cilindrasa marke Audi je {selected_data['CO2 Emissions (g/km)'].mean()} g/km")



# Zadatak pod e
even_cylinders = data[data["Cylinders"] % 2 == 0]
even_cylinders_count = len(even_cylinders)

cylinder_emissions = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
print(cylinder_emissions)



# Zadatak pod f
diesels = data[(data['Fuel Type'] == 'D')]
petrols = data[(data['Fuel Type'] == 'X')]

print(f"Dizeli:\nProsjecno: {diesels['Fuel Consumption City (L/100km)'].mean()} - Medijalno: {diesels['Fuel Consumption City (L/100km)'].median()}")
print(f"Benzinci:\nProsjecno: {petrols['Fuel Consumption City (L/100km)'].mean()} - Medijalno: {petrols['Fuel Consumption City (L/100km)'].median()}")



#Zadatak pod g
four_cylinder_diesels = diesels[(diesels['Cylinders'] == 4)]
print(f"4 cilindricni dizel koji najvise goriva trosi u gradu jest:\n{four_cylinder_diesels.nlargest(1, 'Fuel Consumption City (L/100km)')}")


# Zadatak pod h
manuals = data[(data['Transmission'].str[0] == 'M')]
length = len(manuals['Make'])
print(f"Postoji {length} vozila s rucnim mjenjacem")

#Zadatak pod i
print(data.corr(numeric_only=True).to_string())

#Komentar zadatka pod i: Veličine imaju prilično visoku korelaciju. Na primjer, obujam motora i broj cilindara imaju koeficijent korelacije oko 0.9, dok je korelacija s potrošnjom goriva oko 0.8, što ukazuje na snažnu povezanost. Također, razlog zašto potrošnja izražena u mpg ima veliku negativnu korelaciju jest taj što je ta mjera obrnuta – što vozilo troši više goriva, vrijednost mpg je manja.




