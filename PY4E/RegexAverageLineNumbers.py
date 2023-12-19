import re

# mbox-short.txt
fileName = input("Enter file Name: ")
file = open(fileName)
total = 0
count = 0
for line in file:
    line = line.rstrip()
    x = re.findall("[0-9.]+", line)
    print ("x-->",x)
    if len(x) > 0:
        count += 1
        #total += x

#average = total / count
#print("average:", average)
