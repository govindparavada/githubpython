# mbox-short.txt
#fileName = input("Enter file Name:")
file = open('mbox-short.txt')
hourCount = dict()
fromStart = 'From'
for line in file:
    wordList = line.split()
    if len(line) > 1:
        startWord = wordList[0]
        if fromStart == startWord:
            hourString = wordList[5]
            hourList = hourString.split(':')
            hourStart = hourList[0]
            hourCount[hourStart] = hourCount.get(hourStart, 0) + 1

hours = list()
for hour, count in hourCount.items():
    hours.append((hour, count))

hours.sort()
# print("hours count in sorted order:", hours)

x = tuple()
for hour, count in hours:
    x = (hour, count)
    print(x[0], x[1])
