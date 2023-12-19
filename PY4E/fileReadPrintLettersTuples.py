# mbox-short.txt
import re

fileName = input("Enter File Name: ")
file = open(fileName)
printLetters = dict()
listWords = list()
regexValue = True
for line in file:
    wordList = line.split()
    if len(line) > 1:
        for word in wordList:
            wordLowerCase = word.lower()
            # if re.search('^'[a-z], wordLowerCase):
            listWords.append(wordLowerCase)

print("list words", listWords)
