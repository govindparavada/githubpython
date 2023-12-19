hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

workHours = float(hours)
rate = float(rate)

regularWorkHours = 40
overTimeRate = 1.5
normalRate = 1


def computePay(workHours, rate):

    if workHours > regularWorkHours:
        overTimePay = (workHours -
                       regularWorkHours) * overTimeRate * rate
        regularPay = regularWorkHours * normalRate * rate
        return overTimePay + regularPay
    else:
        regularPay = workHours * normalRate * rate
        return regularPay

print("pay ", computePay(workHours, rate))
