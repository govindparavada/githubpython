# mbox-short.txt
#fileName = input("Enter file: ")
file = open('mbox-short.txt','r')
daysCount = dict()
fromStart = 'From'
for line in file:
    days = line.split()
    if len(days) > 1:
        firstWord = days[0]
        if firstWord == fromStart:
            weekDay = days[2]
            daysCount[weekDay] = daysCount.get(weekDay, 0) + 1

print("days count", daysCount)