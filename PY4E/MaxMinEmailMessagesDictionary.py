#mbox-short.txt
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

key_max = max(emailCount.keys(), key=(lambda k: emailCount[k]))
print('Key Name and Maximum Value: ', emailCount[key_max])
key_min = min(emailCount.keys(), key=(lambda k: emailCount[k]))
print('Key Name and Minimum Value: ', emailCount[key_min])
