string = 'X-DSPAM-Confidence:0.8475'
length = len(string)
colonLocation = string.find(':')
subString = string[colonLocation + 1:length]
print('sub string after colon', subString)
value = float(subString)
print(type(value))
print('float value of sub string is', value)