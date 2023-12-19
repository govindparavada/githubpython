import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("company_sales_data.csv")

#1.	Read Total profit of all months and show it using a line plot
# Total profit data provided for each month. Generated line plot must include the following properties:
# X label name = Month Number
# Y label name = Total profit
# Plot title = Company profit per month
# The graph should look like below:


profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

#2.	Get total profit of all months and show line plot with the following Style properties

profitList = df['total_profit'].tolist()
monthList = df['month_number'].tolist()
plt.plot(monthList, profitList, label='Profit data of last year',
         color='r', marker='o', markerfacecolor='k',
         linestyle='--', linewidth=3)
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

#3.	Read all product sales data and show it using a multiline plot.
# Display the number of units sold per month for each product using multiline plots.
# (i.e., Separate Plotline for each product). Include a plot title, axis names and a legend.
# The graph should look like below:

monthList = df['month_number'].tolist()
faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
shampooSalesData = df['shampoo'].tolist()
moisturizerSalesData = df['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData,   label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')
plt.show()

#4.	Read toothpaste sales data of each month and show it using a scatter plot

monthList  = df ['month_number'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title(' Tooth paste Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.show()

#5.	Read face cream and facewash product sales data and show it using the bar chart.

monthList = df['month_number'].tolist()
faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()
plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and Facecream Sales Data')
plt.show()

#6.	Read sales data of bathing soap of all months and show it using a bar chart. Include a plot title, axis names and a legend.
# Save this plot to your hard disk. The bar chart should look like below:

monthList = df['month_number'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Bathingsoap Sales Data')
plt.savefig('sales_data_of_bathingsoap.png', dpi=150)
plt.show()

#7.	Read the total profit of each month and show it using the histogram to see the most common profit ranges. Include a plot title,
# axis names and a legend. The histogram should look like below:

profitList = df['total_profit'].tolist()
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label = 'Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Profit data')
plt.show()

#8  Calculate total sales data for last year for each product and show it using
#a.	A Pie chart

monthList = df['month_number'].tolist()
labels = ['FaceCream', 'FaceWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(),
         df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()

#8b .	A Horizontal Bar chart
labels = ['FaceCream', 'FaceWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(),
         df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]
data=pd.DataFrame({'labels':labels, 'salesData':salesData})
sorted_data = data.sort_values(by='salesData')
plt.barh(sorted_data.labels, sorted_data.salesData)
plt.xlabel("Sales")
plt.ylabel("Products")
plt.title('Sales Data')
plt.show()

#9.	Read Bathing soap facewash of all months and display it using the Subplot. Include plot titles and axis names.
# The Subplot should look like below:
monthList = df['month_number'].tolist()
bathingsoap = df['bathingsoap'].tolist()
faceWashSalesData = df['facewash'].tolist()

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(monthList, bathingsoap, label = 'Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
axarr[0].set_title('Sales data of  a Bathingsoap')
axarr[1].plot(monthList, faceWashSalesData, label = 'Face Wash Sales Data', color='r', marker='o', linewidth=3)
axarr[1].set_title('Sales data of  a facewash')

plt.xticks(monthList)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.show()


#10.	Read all product sales data and show it using a stack plot. Include a plot title, axis
# names and a legend.The Stack plot should look like below:

monthList = df['month_number'].tolist()
faceCremSalesData = df['facecream'].tolist()
faceWashSalesData = df['facewash'].tolist()
toothPasteSalesData = df['toothpaste'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
shampooSalesData = df['shampoo'].tolist()
moisturizerSalesData = df['moisturizer'].tolist()
plt.plot([],[],color='m', label='face Cream', linewidth=5)
plt.plot([],[],color='c', label='Face wash', linewidth=5)
plt.plot([],[],color='r', label='Tooth paste', linewidth=5)
plt.plot([],[],color='k', label='Bathing soap', linewidth=5)
plt.plot([],[],color='g', label='Shampoo', linewidth=5)
plt.plot([],[],color='y', label='Moisturizer', linewidth=5)
plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData,
              bathingsoapSalesData, shampooSalesData, moisturizerSalesData,
              colors=['m','c','r','k','g','y'])
plt.xlabel('Month Number')
plt.ylabel('Sales Units in Number')
plt.title('All Product Sales Data Using Stack Plot')
plt.legend(loc='upper left')
plt.show()

import seaborn as sns
df = pd.read_csv("titanic.csv")

#11.	Use the jointplot function on fare and age. The function jointplot draws a plot of two variables
# with bivariate and univariate graphs.

x = 'Fare'
y = 'Age'
kind = 'scatter'
sns.jointplot(x=df[x], y=df[y], kind = kind)
plt.show()

#12.  Plot the boxplots of the classes over the age of the people. The boxplot function draws a box plot to
# show distributions with respect to categories.

x = 'Pclass'
y = 'Age'
sns.boxplot(data=df, x=df[x], y=df[y])
plt.show()

#13. Use the countplot function to count the number of male and female in the dataset. The function countplot shows
# the counts of observations in each categorical bin.

x = 'Sex'
sns.countplot(data=df, x=df[x])
plt.show()

#14.Use the heatmap function to plot the correlation between the columns of the dataset.
sns.heatmap(df.corr(), cmap='coolwarm')
plt.title('titanic.corr()')
plt.show()
