#1.	A five-digit number is entered through the keyboard. Write a program to obtain
# the if this number is palindrome.

num = int(input("Enter 5 digit Number: "))
a=num
sum=0
while(num>0):
	rem=num%10
	sum=(sum*10)+rem
	num=num//10
if(a==sum):
	print("It's a palindrome")
else:
	print("It's not a palindrome")

#2. Ages of three people are input through the keyboard, write a program to determine
# the youngest of the three.

age1 = int(input("Enter the Age of A :"))
age2 = int(input("Enter the Age of B :"))
age3 = int(input("Enter the Age of C :"))
if(age1<age2 and age1<age3):
	print("The Youngest Age is A")
elif(age2<age1 and age2<age3):
	print("The Youngest Age is B")
else:
	print("The Youngest Age is C")

#3. Write a program to find the reverse of n digit number using While loop

num = int(input("Enter the Number: "))
a=num
sum=0
while(num>0):
	rem=num%10
	sum=(sum*10)+rem
	num=num//10
print("Before Number :",a)
print("Reverse Number :",sum)

#4	Write a Python program to remove all the occurrences of an element from a list
val = [1, 3, 4, 6, 5, 1]
a = 1
print ("Original list :" ,val)
c = val.count(a)
for i in range(c):
    val.remove(a)
print ("Remove operation :" , val)

#5 	Write a Python program to reverse All Strings in String List
val = ["Tutor", "joes", "Computer", "Education"]
print("Original list : ", val)
res = [i[::-1] for i in val]
print("Reversed list : ", res)

#Another way
val = ["Tutor", "joes", "Computer", "Education"]
print("Original list : ", val)
print("Reversed list : ", val[::-1])

#6.	Write a Python program to reverse a tuple.
a = (23, 45, 67, 78, 89, 90, 34, 56)
print("Before Reverse :", a)
print("After Reverse :",a[::-1])

#Second Method
a = (23, 45, 67, 78, 89, 90, 34, 56)
print("Before Reverse :", a)
b = list(a)
b.reverse()
a = tuple(b)
print("After Reverse :",a)

# Third Method
a = (23, 45, 67, 78, 89, 90, 34, 56)
print("Before Reverse :", a)
y = reversed(a)
print("After Reverse :", tuple(y))

#7.	Write a Python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x)
l = int(input("Enter the Limit : "))
d = dict()

for x in range(1, l + 1):
	d[x] = x * x
print(d)

#8.	Write a program to sum all the values of a dictionary.
marks = {"m1": 92, "m2": 56, "m3": 88, "m4": 97, "m5": 89}
total = []
for i in marks.values():
	total.append(i)
print("Sum of Values :", sum(total))

#9.	Write a Python program to get a string from a given string where all occurrences of
# its first char have been changed to "@", except the first char itself
#Example: Information Analytics should be Informat@on Analyt@cs after change

str="Information Analytics"
print("Given String :",str)
str_lower = str.lower()
ch = str_lower[0]
str = str.replace(ch, '@')
str = ch + str[1:]
print("After String :",str)

#10.	Write a python program to create a simple calculator (Add, Subtract, Multiply and Division).
# Use functions.

def add(P, Q):
	# This function is used for adding two numbers
	return P + Q

def subtract(P, Q):
	# This function is used for subtracting two numbers
	return P - Q

def multiply(P, Q):
	# This function is used for multiplying two numbers
	return P * Q

def divide(P, Q):
	# This function is used for dividing two numbers
	return P / Q

# Now we will take inputs from the user
print("Please select the operation:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice (a/ b/ c/ d): ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
	print(num_1, " + ", num_2, " = ", add(num_1, num_2))
elif choice == 'b':
	print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))
elif choice == 'c':
	print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))
elif choice == 'd':
	print(num_1, " / ", num_2, " = ", divide(num_1, num_2))
else:
	print("This is an invalid input")

#11. Open the file mbox-short.txt (Use try and except) and print all the lines started with “From:”
try:
	fhand = open('mbox-short.txt')
except:
	print("There is some  error")
	exit()
for line in fhand:
    line = line.strip()
    if line.startswith('From:'):
        print(line)

#12.	Delete the second column from a given array and insert the following new column in its place
import numpy
print("Printing Original array")
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)
print("Array after deleting column 2 on axis 1")
sampleArray = numpy.delete(sampleArray , 1, axis = 1)
print(sampleArray)
arr = numpy.array([[10,10,10]])
print("Array after inserting column 2 on axis 1")
sampleArray = numpy.insert(sampleArray , 1, arr, axis = 1)
print(sampleArray)

#13. Count total number of Cars per company in the automobile data and save the result in an csv file.
import pandas as pd
df = pd.read_csv("Automobile_data.csv")
cnt_by_company = df['company'].value_counts()
cnt_by_company.to_csv("Count by Company.csv")

