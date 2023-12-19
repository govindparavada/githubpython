#1.Write a program to read through a file and print the contents of the file (line by line)
# all in uppercase. (Use the abc.txt file)

fh = open('abc.txt')
for line in fh:
    print(line.upper().strip())

#2.Write a function in Python to count the number of lines from a text file
# that does not start with "T". (Use the abc.txt file)

def line_count():
    file = open("abc.txt","r")
    count = 0
    for line in file:
        if line[0] not in 'T':
            count += 1
    file.close()
    print("No of lines not starting with 'T'=",count)

line_count()

# 3.Write a function in Python to read lines from a text file. Your function should find and
# display the number of occurrences of the word "the". (Use the abc.txt file)

def count_words():
    file = open("abc.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word.upper() == "THE":
            count += 1
    print("THE--", count)
    file.close()

count_words()

# 4.Write a program that repeatedly prompts a user for integer numbers until the user enters “done”,

num_list = []
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    num_list.append(int(num))

print("Maximum number is ", max(num_list))
print("Minimum number is ", min(num_list))

#5.Write a program that rotates the element of a list so that the element at the first index moves
# to the second index, the element in the second index moves to the third index, etc.,
# and the element in the last index moves to the first index.

mylist = []
size = int(input('How many elements you want to enter? '))
print('Enter', str(size), 'elements')
for i in range(size):
    data = input()
    mylist.append(data)
print('list before shifting', mylist)
temp = mylist[size - 1]
for i in range(size - 1, 0, -1):
    mylist[i] = mylist[i - 1]
mylist[0] = temp
print('list after shifting', mylist)

# 6.Write a program that reads the words in words.txt, stores them as keys in a dictionary and assigns as
# values the number of occurrences of each word. (Use the words.txt file)

text = open("words.txt", "r")
d = dict()
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
for key in list(d.keys()):
    print(key, ":", d[key])

# 7.Write a program to accept the name, surname, and phone number of the user repeatedly until
# the user enters “done.” Write all the data collected from the user to a .txt file in the following format.
# Name1 Surname1 Number1 Name2 Surname2 Number2 … NameN SurnameN NumberN

contact = []
while True:
    name = input("Enter Name: ")
    if name == 'done':
        break
    surname = input("Enter Surname: ")
    num = input("Enter Number: ")
    contact.append(name)
    contact.append(surname)
    contact.append(num)
    with open('contacts.txt', 'a') as f:
        line = contact[0] + ' ' + contact[1] + ' ' + contact[2] + '\n'
        f.write(line)
    contact.clear()

# 8.Read the file generated in Q7 as a dictionary with the tuple (name, surname) as the key
# and the number as the value.

contacts = {}
with open("contacts.txt", 'r') as f:
    line = f.readline()
    while line:
        tokens = line.split()
        name, surname, number = tokens[0], tokens[1], tokens[2]
        contacts[name, surname] = number
        line = f.readline()
print(contacts)

#9.Write a menu that allows the user to perform the following actions until the digit 7 is pressed:

def printContacts(contacts):
    for key, value in contacts.items():
        print(key[0] + ' ' + key[1] + ' ' + value)


def sortByName(contacts):
    return dict(sorted(contacts.items()))


def sortBySurname(contacts):
    swapDict = {}
    for key, value in contacts.items():
        swapDict[key[1], key[0]] = value
    swapDict = sortByName(swapDict)
    sortedDict = {}
    for key, value in swapDict.items():
        sortedDict[key[1], key[0]] = value
    return sortedDict


def saveContacts(contacts, filename):
    with open(filename, 'w') as f:
        for key, value in contacts.items():
            line = key[0] + ' ' + key[1] + ' ' + value + '\n'
            f.write(line)


contacts = {}
with open("contacts.txt", 'r') as f:
    line = f.readline()
    while line:
        tokens = line.split()
        name, surname, number = tokens[0], tokens[1], tokens[2]
        contacts[name, surname] = number
        line = f.readline()
print(contacts)

print("What would you like to do?")
print("1 - Sort by name")
print("2 - Sort by surname")
print("3 - Save as a file")
print("4 - Add new contact")
print("5 - Print contacts")
print("6 - Delete contact")
print("7 - Exit")
option = input()
while option != '7':
    if option == '1':
        contacts = sortByName(contacts)
        printContacts(contacts)
    elif option == '2':
        contacts = sortBySurname(contacts)
        printContacts(contacts)
    elif option == '3':
        saveContacts(contacts, 'contacts2.txt')
        print('Contacts saved')
    elif option == '4':
        print('Insert name')
        name = input()
        print('Insert surname')
        surname = input()
        print('Insert number')
        number = input()
        contacts[name, surname] = number
        printContacts(contacts)
    elif option == '5':
        printContacts(contacts)
    elif option == '6':
        print('Insert name')
        name = input()
        print('Insert surname')
        surname = input()
        try:
            key = tuple((name, surname))
            contacts.pop(key)
        except:
            print("Contact not found")
        printContacts(contacts)
    else:
        print('Type again')
    print("What would you like to do?")
    print("1 - Sort by name")
    print("2 - Sort by surname")
    print("3 - Save as a file")
    print("4 - Add new contact")
    print("5 - Print contacts")
    print("6 - Delete contact")
    print("7 - Exit")
    option = input()



