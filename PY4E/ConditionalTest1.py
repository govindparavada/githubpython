hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

workHours = float(hours)
rate = float(rate)

regularHours = 40

if workHours <= regularHours:
    print('normal hours worked and pay is:', workHours * rate)
else:
    overTimeHours = workHours - regularHours
    overTimeRate = rate * 1.5
    print('over time worked and pay is:', (regularHours * rate)+(overTimeHours * overTimeRate))
