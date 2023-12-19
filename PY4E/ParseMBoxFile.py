# mbox-short.txt
fileName = input("Enter a File: ")
file = open(fileName)
count = 0
for line in file:
    line = line.rstrip()
    wordList = line.split()
    if len(wordList) > 1:
        firstWord = wordList[0]
        if firstWord == 'From':
            eMail = wordList[1]
            print(eMail)
            count = count + 1

print("There were "+str(count)+" lines in the file with From as the first word")
