import pandas as pd
#1 From given data set, print first and last five rows
# Read csv file using pandas, use head and tail functions from DataFrame objects.

df = pd.read_csv("Automobile_data.csv")
df.head(5)
df.tail(5)

#2 Clean data and update the CSV file. Replace all column values which contain ‘?’ and n.a with NaN.

df = pd.read_csv("Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
#print (df)

df.head(6)

#SAVE FILE
df.to_csv("Automobile_data2.csv")

#3 Find the most expensive car company name. Print the most expensive car’s company

df = pd.read_csv("Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
df

#4 Print All Toyota Cars details groupby and get_group

df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
toyotaDf

#5 Count total cars per company
# value_counts()

df = pd.read_csv("Automobile_data.csv")
df['company'].value_counts()