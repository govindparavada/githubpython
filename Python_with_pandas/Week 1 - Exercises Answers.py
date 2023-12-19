
# Assign a value to a variable and find the type of variable
x = 26
print("type of variable", type(x))


"""
1.	Write a program to accept a string from the user and display it twice.
For example, if the user enters a string as "hello", the output should be "hello hello".
"""

str = input("Please enter string: ")
print(str*2)



"""
2.	Write a program to accept two integer numbers from users and display their product and sum.
"""
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

print(num1*num2)
print(num1 + num2)


"""
3.	Given two integer numbers return their product and if the product is greater than 1000, then return their sum.
"""
num1_prod = 200
num2_prod = 100

prod = num1_prod * num2_prod
sum_numbers = num1_prod + num2_prod 
if(prod > 1000):
    print(sum_numbers)
else:
    print(prod)
    

"""
4.	Write a program to accept an integer from the user. Depending on whether the number is even or odd, print out an appropriate message to the user. 
"""

int_num = int(input("Enter an integer number"))
if(int_num%2 == 0):
    print("It is an even number")
else:
    print("Its is an odd number")
    
"""
5.	Write a program to divide two numbers. Handle exception using try-except to handle ZeroDivisionError. 
"""

num1_div = 2000
num2_div = 0
try:
    res = num1_div / num2_div
    print("Result is: "+ res)
except:
    print("Divide by 0 exception. Denominator should not be 0 !!!")
    
"""
6.	Write a program to print the grade of the student. A school has the following rules for the grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask the user to enter marks and print the corresponding grade.

"""
marks = int(input("Enter student marks: "))
if(marks < 25):
    print("F")
elif(marks >= 25 and marks < 45):
    print("E")
elif(marks >= 45 and marks < 50):
    print("D")
elif(marks >= 50 and marks < 60):
    print("C")
elif(marks >=60 and marks < 80):
    print("B")
else:
    print("A")
    
"""
7.	A student will not be allowed to sit in an exam if his/her attendance is less than 75%.
Take the following input from the user:
•	Number of classes held
•	Number of classes attended.
And print percentage of class attended
Is the student allowed to sit in the exam or not?
"""

classes_held = int(input("Enter classes held: "))
classes_attended = int(input("Enter classes attended: "))

percentage_classes_attended = classes_attended/classes_held * 100

print(percentage_classes_attended)

if(percentage_classes_attended > 75):
    print("Allowed")
else:
    print("Not allowed")













