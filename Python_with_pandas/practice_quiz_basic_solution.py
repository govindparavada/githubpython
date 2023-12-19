#!/usr/bin/python
# coding=<utf-8>

"""
IS6061 - Python Basic Quiz Solutions (basic)
============================================

@Authors: Lalita Lalwani, Sabarish Nair & Selja Seppälä

All the answers are inside functions to facilitate the code in Q6.
However, the content of each function corresponds to
a possible solution for each question.
You can run the solution to each question separately
by commenting all the other function calls at the end of the file.
"""

# Q1
def print_file():
    # Open the file for reading
    file = open('contacts.txt','r')
    # Read the file and print it
    print(file.read())

# Q2
def print_formatted_records():
    # Open the file for reading.
    file = open('contacts.txt','r')

    # Create a counter that is incremented
    # at each new line being read from the file,
    # remove any leading/trailing characters of the line and
    # split the line to print out the required elements.
    counter = 0
    for line in file:
        counter = counter + 1
        record = line.strip().split()
        phone, name, surname, age = record[0], record[1], record[2], record[3]
        # You can also use the right-hand side elements directly in the print statement
        print(counter, phone, name, surname, "(" + age + ")")

# Q3
def get_phone_number():
    # Open the file for reading
    file = open('contacts.txt','r')

    # Ask user to input a name and,
    # if the name is in the current line,
    # remove any leading/trailing characters,
    # split the line to get the phone number
    # and print it with the country code.
    name = input('Enter full name: ')
    for line in file:
        if name in line:
            print('00353' + line.strip().split()[0])

# Q4
def add_new_record():
    # Ask user to input required information
    # and create a new record string
    # with a new line and
    # the same format as the existing records:
    # "\n" + phone + "\t" + full_name + "\t" + age
    # where first and last name in full_name
    # are separated by a space.
    # Append the string to the file.
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    age = input("Enter age: ")
    new_record = "\n" + phone + "\t" + first_name + " " + last_name + "\t" + age

    with open('contacts.txt','a') as file:
        file.write(new_record)

# Q5
def get_youngest():
    """Find the youngest person in the database."""
    # Open the file for reading.
    file = open('contacts.txt', 'r')

    # Variables to keep track of
    # the youngest person so far
    # and related information.
    youngest = None
    youngest_info = ''

    # If youngest is None, assign it the age being read,
    # otherwise test if the age being read
    # is smaller than youngest.
    # If it is, replace the value of youngest
    # with the current age.
    # Once all records have been read,
    # print out the information of the youngest person.
    for line in file:
        current_age = line.strip().split()[-1]
        if youngest is None:
            youngest = current_age
        elif current_age < youngest:
            youngest = current_age
            youngest_info = line
    print('The youngest person is:', youngest_info)

# Q6
def print_names():
    # Open the file for reading.
    file = open('contacts.txt', 'r')

    # At each new line being read from the file,
    # remove any leading/trailing characters of the line and
    # split the line to print out the first and last names.
    for line in file:
        record = line.strip().split()
        print(record[1], record[2])

def display_menu():
    print("\nPlease select an option from the following menu:")
    print("1 - Print all names")
    print("2 - Return phone number with country code based on name")
    print("3 - Add a new record")
    print("4 - Get youngest person")
    print("5 - Exit")

def menu_program():
    # Display the options menu and
    # get user input
    display_menu()
    option = input()

    # Execute selected options 1-4,
    # exit with 5, and
    # print message for all other options.
    while option != '5':
        if option == '1':
            print_names()
        elif option == '2':
            get_phone_number()
        elif option == '3':
            add_new_record()
        elif option == '4':
            get_youngest()
        else:
            print('\nThis is not a valid option, please try again.')

        display_menu()
        option = input()

# Main program starts here
# Q1
#print_file()
# Q2
# print_formatted_records()
# Q3
# get_phone_number()
# Q4
# add_new_record()
# Q5
# get_youngest()
# Q6
menu_program()