i = 0
numberList = list()
while i == 0:
    number = input("Enter a number: ")
    if number == 'done':
        i = i + 1
    else:
        numberList.append(number)

print("Minimum number in the list is :", min(numberList))
print("Maximum number in the list is :", max(numberList))
