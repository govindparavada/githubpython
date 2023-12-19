# -*- coding: utf-8 -*-
"""
IS6061 - Python Basic Quiz Solutions (more elaborate)
=====================================================

@Authors: Lalita Lalwani, Sabarish Nair & Selja Seppälä
"""
contacts = dict()

#Question 1: Function to read from file based on file name and mode
def readFromFile(fileName, mode):
    try:
        with open(fileName,mode) as fileHandle:
            for lines in fileHandle:
                lines = lines.rstrip().split()
                # lines = lines.split()
                contacts[lines[0]] = lines[1]+' '+lines[2]+' '+lines[3]
             
            return contacts
    except:
        return -1

#Q1: Print all records post import
def printAllRecords():
    for key in contacts:
        print(key, contacts[key])

#Q6.1: Function to print all names
def printNames():
    for key in contacts:
        print(contacts[key].split()[0]+" "+contacts[key].split()[1])

#Q2: Print details with line numbers
def printDetailsWithLineNumber():
    for idx,key in enumerate(contacts):
        personal_details = contacts[key].split()
        displayFormattedRecords(str(idx+1),personal_details[0], personal_details[1],key,personal_details[2])

#Q2: display Records with formatted line numbers
def displayFormattedRecords(line_num, first_name, surname, phone_num, age):
    print(f"{line_num} {first_name} {surname} {phone_num} ({age})")

#Q3: Get phone number based on name
def getPhoneNumberFromName():
    try:
        countrycode = '00353'
        name = input("Enter Name: ")
        searchResults = {k:contacts[k].rsplit()[0]+" "+contacts[k].rsplit()[1] for k in contacts if contacts[k].rsplit()[0]+" "+contacts[k].rsplit()[1] == name}
        if len(searchResults) == 0:
            print("No match found in records!")
        else:
            for key in searchResults:
                print(countrycode+key)
    except:
        print("Some error!")

#Q4: Add new record to file
def addNewRecordToContacts():
    name = input("Enter first name and surname: ")
    phonenum = input("Enter phone number: ")
    age = input("Enter age: ")
    addNewContactToFile("\n"+phonenum+"\t"+name +"\t"+age)

#Q4: Append new record to file
def addNewContactToFile(new_record):
        with open(filepath,'a') as fHandle:
            fHandle.write(new_record)

#Q5: Returns record of youngest person
def getYoungestPerson():
    # Get the age of the first person
    # (as the youngest person so far when the loop starts)
    first_value = int(list(contacts.values())[0].split()[2])

    # Keep track of the key in the contacts dict
    # corresponding to the youngest person so far
    required_key = ""
    for key in contacts:
        # Check if the age in the record
        # currently being read is
        # smaller than the youngest age so far.
        if(int(contacts[key].split()[2]) < first_value):
            # If it is the case, update the new youngest age
            # and store the key in the contacts dict
            # corresponding to the youngest person so far
            first_value = int(contacts[key].split()[2])
            required_key = key
    
    print(required_key, contacts[required_key])

#Q6: Function used to display Menu to user
def displayMenu():
    print("\nPlease select an option from the following menu:")
    print("1 - Print all names")
    print("2 - Return phone number with country code based on name")
    print("3 - Add a new record")
    print("4 - Get youngest person")
    print("5 - Exit")

# Main program starts here
filepath = 'contacts.txt'
contacts = readFromFile(filepath,'r')

# You can (un)comment the function calls
# to run them individually.
# Q1
printAllRecords()

# Q2
printDetailsWithLineNumber()

# Q3
getPhoneNumberFromName()

# Q4
addNewRecordToContacts()

# Q5
getYoungestPerson()

# Q6
displayMenu()
option = input()

while option!= '5':
    if option == '1':
        printNames()
    elif option == '2':
        getPhoneNumberFromName()
    elif option == '3':
        addNewRecordToContacts()
    elif option == '4':
        getYoungestPerson()
    else:
        print('\nThis is not a valid option, please try again.')

    displayMenu()
    option = input()
