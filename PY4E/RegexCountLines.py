import re

# ^ Received
userRegex = input("Enter a regular expression: ")
# mbox-short.txt
fileName = input("Enter file Name: ")
file = open(fileName)
count = 0
for line in file:
    line = line.rstrip()
    x = re.findall("^Received:.*", line)
    if len(x)>0:
        count+=1

print(fileName+" had "+str(count)+" lines that matched "+ userRegex)


