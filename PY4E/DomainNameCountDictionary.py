# mbox-short.txt
fileName = input("Enter a file name: ")
file = open(fileName)
fromStart = 'From'
domainCount = dict()
for line in file:
    if len(line) > 1:
        line = line.rstrip()
        wordList = line.split()
        startWord = wordList[0]
        if startWord == fromStart:
            eMail = wordList[1]
            domainList = eMail.split('@')
            domain = domainList[1]
            domainCount[domain] = domainCount.get(domain, 0) + 1

print("domainCount:", domainCount)
