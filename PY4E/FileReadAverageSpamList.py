# mbox-short.txt
fileName = input("Enter file Name: ")
handle = open(fileName, 'r')
file = handle.read()
spam = "X-DSPAM-Confidence: 0.8475"
floatConfidence = 0
floatConfidenceSPAMValue = 0.8475
count = 0
for line in file:
    if line not in (spam):
        continue
    floatConfidence = floatConfidence + floatConfidenceSPAMValue
    count = count + 1

averageSpam = floatConfidence / count
print("Average spam confidence:", averageSpam)
