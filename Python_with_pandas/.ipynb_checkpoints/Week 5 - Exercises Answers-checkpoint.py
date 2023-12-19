#Import all the libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Load the data in a dataframe
df = pd.read_csv('customerdata.csv')

#1. Find the total number of rows and columns in the customerdata.csv file.
print(df.shape)

#2. Are there any missing values in the dataset? If yes, then find how many in which column.
print(df.isna().sum())

#3. Calculate the mean credit score for each income group.
print(df.groupby(by="income")["credit_score"].mean())

#4.
#Create a function to update values with average mean credit score of that particular income class
def update_credscore(incomeclasses):
    for ic in incomeclasses:
        mask = df['income'] == ic
        mean = df[df['income'] == ic] ['credit_score'].mean()
        df.loc[mask,'credit_score'] = df.loc[mask,'credit_score'].fillna(mean)

#Updating the values
diffincomegroups = df.income.unique()
update_credscore(diffincomegroups)


#5. Update the average annual mileage where it is null/NA.
avg_mileage = df["annual_mileage"].mean()
df["annual_mileage"].fillna(avg_mileage,inplace=True)


#6. What is the correlation among different variables? Plot that on a heatmap.
print(df.corr())
sns.heatmap(df.corr())
plt.title("Correlation between Selected Variables")
plt.show()


