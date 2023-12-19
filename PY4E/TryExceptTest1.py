hours = input('Enter Hours: ')
rate = input('Enter rate: ')

try:
    floatHours = float(hours)
    floatRate = float(rate)
    print('Pay :', floatHours / floatRate)
except Exception as e:
    print('Error, please enter numeric input---', e)
