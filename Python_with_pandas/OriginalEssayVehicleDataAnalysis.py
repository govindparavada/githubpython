import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# the most common vehicle model shown in pie chart – refer figure 7 for output
labels = dfm["vehicle_model"][:30].value_counts().index
sizes = dfm["vehicle_model"][:30].value_counts()
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', "blue", "yellow"]
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, rotatelabels=False, autopct='%1.1f%%', colors=colors, shadow=True, startangle=45)
plt.title('Vehicle Model Name', color='red', fontsize=15)
plt.show()

# frequency of each unique value in the column “manf_year”
dfm.manf_year.value_counts()

# vehicles manufactured in year in bar chart-refer figure 8 for output
sns.countplot(data=dfm,x="manf_year",palette="icefire")
plt.xticks(rotation=90)
plt.xlabel("Manufactured Year",fontsize=10,color="red")
plt.ylabel("Count",fontsize=10,color="red")
plt.title("Year Count",color="red")
plt.show()

# vehicles manufactured in year in pie chart - refer figure 9 for output
labels = dfm["manf_year"][:40].value_counts().index
sizes = dfm["manf_year"][:40].value_counts()
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99',"pink","red"]
plt.figure(figsize = (8,8))
plt.pie(sizes, labels=labels, rotatelabels=False, autopct='%1.1f%%',colors=colors,shadow=True, startangle=45)
plt.title('Manufactured Year',color = 'red',fontsize = 15)
plt.show()

# frequency of each unique value in the column “fuel_type”
dfm.fuel_type.value_counts()

# vehicles by fuel type in pie chart - refer figure 10 for output
labels = dfm["fuel_type"].value_counts().index
sizes = dfm["fuel_type"].value_counts()
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99',"blue","pink"]
plt.figure(figsize = (8,8))
plt.pie(sizes, labels=labels, rotatelabels=False, autopct='%1.f%%',colors=colors,shadow=True, startangle=9)
plt.title('Fuel Type',color = 'RED',fontsize = 15)
plt.show()

# frequency of each unique value in the column “seller_type”
dfm.seller_type.value_counts()

# this chart shows how the sales are made in bar chart - refer figure 11 for output
sns.countplot(data=dfm,x="seller_type",palette="CMRmap")
plt.xlabel("Seller Type",fontsize=10,color="red")
plt.ylabel("Count",fontsize=10,color="red")
plt.title("Seller Type Count",color="red")
plt.show()

# frequency of each unique value in the column “owner_type”
dfm.owner_type.value_counts()

# this chart shows owner count in bar chart - refer figure 12 for output
sns.countplot(data=dfm,x="owner_type",palette="viridis")
plt.xlabel("Owner",fontsize=10,color="red")
plt.ylabel("Count",fontsize=10,color="red")
plt.title("Owner Count",color="red")
plt.show()

# this chart shows owner type in pie chart - refer figure 12 for output
labels = dfm["owner_type"].value_counts().index
sizes = dfm["owner_type"].value_counts()
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99',"yellow","red"]
plt.figure(figsize = (8,8))
plt.pie(sizes, labels=labels, rotatelabels=False, autopct='%1.1f%%',colors=colors,shadow=True, startangle=905)
plt.title('owner',color = 'red',fontsize = 15)
plt.show()

# histogram showing the distribution of manual and automatic cars by years - refer figure 13 for output
sns.histplot(data=dfm, x="manf_year", hue="transmission")
plt.xticks(rotation=45)
plt.show()

# violin graph showing the distribution of manual and automatic cars by years - refer figure 14 for output
sns.violinplot(data=dfm, x="manf_year", y="fuel_type",hue="transmission")
plt.show()


