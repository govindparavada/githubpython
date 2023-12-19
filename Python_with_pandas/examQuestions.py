import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
print(df.head(1))
df.hist(column='facewash');
df.plot(kind='hist')
df.plot.hist()

#box plot
plt.boxplot(df)

names = []
marks = []

marksDict =dict()


f = open('Marks.txt', 'r')
for row in f:
    row = row.split(' ')
    names.append(row[0])
    marks.append(int(row[1]))
    marksDict[row[0]] = marksDict.get(row[0], 0) + 1

print(marksDict)

#bar chart
plt.bar(names, marks, color='g', label='File Data')

#histogram
plt.hist(marksDict, color='g', label='File Data')


#plt.xlabel('Student Names', fontsize=12)
#plt.ylabel('Marks', fontsize=12)

plt.title('Students Marks', fontsize=20)
plt.legend()
plt.show()

