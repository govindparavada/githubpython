import pandas as pd
import pandas_profiling as pp

# Loading Dataset from CSV file
dfm = pd.read_csv("FourWheelerVehicleDataAnalysis.csv")

# top 10 records from the dataset – refer figure 1 for output
print(dfm.head(10))
# print(dfm)

# row count and type of each column information – refer figure 2 for output
print(dfm.info())

# row  and column information about dataset – refer figure 3 for output
print(dfm.shape)

# numerical values such as mean, standard deviation, min and max information about dataset – refer figure 4 for output
print(dfm.describe())

# number of null values in the data set – refer figure 5 for output
print(dfm.isnull().sum())

# names of the columns in the data set – refer figure 6 for output
print(dfm.columns)

# identify the make of the vehicles model in column named "vehicle_name" and saved as new variable "vehicle_model"
dfm["vehicle_model"] = dfm.vehicle_name.apply(lambda z: ' '.join(z.split(' ')[:1]))

# frequency of each unique value in the column “vehicle_model”
dfm.vehicle_model.value_counts()

pp.ProfileReport(dfm)




