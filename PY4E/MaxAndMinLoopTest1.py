number = ""
minNumber = 0
maxNumber = 0
strDone = "done"

while number != strDone:
    number = input("Enter a Number ")
    try:
        if number == strDone:
            break
        elif float(number) >= maxNumber:
            maxNumber = float(number)
        else:
            minNumber = float(number)
    except Exception as e:
        print("Invalid Input --",e)

print("MaxNumber ", int(maxNumber))
print("MinNumber ", int(minNumber))
