number = 0
count = 0
total = 0
average = 0

strDone = "done"
while number != strDone:
    number = input("Enter a Number ")
    try:
        total = total + float(number)
        count = count + 1
    except Exception as e:
        if number == strDone:
            break
        print("Invalid Input --", e)

print("Sum ", total)
print("Count ", count)
print("Average", total / count)
