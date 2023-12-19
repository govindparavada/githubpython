# mbox-short.txt
fileName = input("Enter file name: ")
file = open(fileName)
fromStart = 'From'
emailCount = dict()
for line in file:
    wordList = line.split()
    if len(line) > 1:
        startWord = wordList[0]
        if fromStart == startWord:
            email = wordList[1]
            emailCount[email] = emailCount.get(email, 0) + 1

tupList = list()
for email, count in emailCount.items():
    # print("emailCountitem:",emailCount)
    tupList.append((count, email))

tupList.sort(reverse=True)
# print("tupList in reverse order:",tupList)

print("Person who has most commits count:", tupList[0])
