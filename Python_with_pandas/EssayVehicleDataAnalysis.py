import pandas as pd
import pandas_profiling as pp

# Loading Dataset from CSV file
dfm = pd.read_csv("FourWheelerCarDataAnalysis.csv")

# top 10 records from the dataset – refer figure 1 in output
print(dfm.head(10))

# row count and type of each column information – refer figure 2 in output
print(dfm.info())

# row  and column information about dataset – refer figure 3 in output
print(dfm.shape)

# numerical values such as mean, standard deviation, min and max information about dataset
# – refer figure 4 in output
print(dfm.describe())

# number of null values in the data set – refer figure 5 in output
print(dfm.isnull().sum())

# names of the columns in the data set – refer figure 6 in output
print(dfm.columns)

# identify the make of the vehicles model in column named "vehicle_name" and saved
# as new variable "vehicle_model"
dfm["vehicle_model"] = dfm.vehicle_name.apply(lambda z: ' '.join(z.split(' ')[:1]))

# frequency of each unique value in the column “vehicle_model”– refer figure 7 in output
dfm.vehicle_model.value_counts()

#pandas profiling report list down overview, variables, Interactions, corelations, missing values
# and samples in detailed manner- refer figure 8 in output
pp.ProfileReport(dfm)
