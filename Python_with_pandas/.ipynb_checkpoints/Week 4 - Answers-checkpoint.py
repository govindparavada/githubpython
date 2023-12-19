#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tutorial 4 Solutions

@author: Sabarish Nair and Lalita Lalwani
"""

#Numpy
#1 Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.
# np.zeros, np.ones


import numpy as np
array = np.zeros(10)
print('zero', array)
array = np.ones(10)
print('ones', array)
array = np.ones(10)*5
print('fives', array)

#2 Create an array of integers from 20 to 80
# np.arange

import numpy as np
array = np.arange(20,81)
print(array)

#3 Create an array of all the even integers from 20 to 80
# np.arange (with different parameters)


import numpy as np
array = np.arange(20, 81, 2)
print('even', array)

#4 Write a NumPy program to create a 4x4 identity matrix.
# np.identity


import numpy as np
array_2D = np.identity(4)
print(array_2D)

#5 Write a NumPy program to create a vector of length 10 with values evenly distributed
# between 5 and 50.

import numpy as np
array = np.linspace(5, 50, 10)
print(array)

#6 Write a NumPy program to create a vector with values ranging from 10 to 35 and
# print all values except the first two elements and the last three elements.
# NumPy array indexing is equivalent to list indexing

import numpy as np
array = np.arange(10, 36)
print('original', array)
print('filtered', array[2:-3])

#7 Write a NumPy program to create a vector with values from 0 to 20 and change the
# sign of the numbers in the range from 9 to 15.
# NumPy array indexing can include also Boolean conditions

import numpy as np
array = np.arange(21)
print(array)
array[(array >= 9) & (array <= 15)] *= -1
print(array)

#8 Write a NumPy program to generate an array of 15 random numbers from a standard
# normal distribution.

import numpy as np
array = np.random.randn(15)
print(array)

#random number between 0 and 1
random_number = np.random.random()
print(random_number)

#9 Write a NumPy program to generate an array of 15 random integers between 10 and 100.
# np.random.randint
import numpy as np
array = np.random.randint(10, 101, 15)
print(array)

#Pandas

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












