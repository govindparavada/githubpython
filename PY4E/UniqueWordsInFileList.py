# "romeo.txt"
fileName = input("enter file name: ")
file = open(fileName)
uniqueWords = list()

for line in file:
    wordList = line.split()

    for word in wordList:
        if word not in uniqueWords:
            uniqueWords.append(word)

uniqueWords.sort()
print("uniqueWords in sorted order list are: ", uniqueWords)
