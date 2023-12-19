# mbox-short.txt
fileName = input("Enter file: ")
file = open(fileName)
fromStart = "From"
emailCount = dict()
for line in file:
    eMails = line.split()
    if len(eMails) > 1:
        firstWord = eMails[0]
        if firstWord == fromStart:
            mail = eMails[1]
            emailCount[mail] = emailCount.get(mail, 0) + 1

print("eMails count", emailCount)
