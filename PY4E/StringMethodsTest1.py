string = 'today weather temperature is 13 degrees and celcius and customer care mail id weathertemerature@test.com'
print('length of string', len(string))
print('first blank space position', string.find(' '))
print('slice of string 1', string[6:51])
print('slice of string 2', string[14:78])
print('boolean degree','degree' in string)
print('boolean Mail','Mail' in string)
print('count of t letter is', string.count('t'))