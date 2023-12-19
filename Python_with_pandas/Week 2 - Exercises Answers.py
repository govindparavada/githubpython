#1. Create a function that accepts as input a number 
#and then prints out a list of all the divisors of that number.
#"""

def print_divisors(n):
    div = 1
    while div <= n:
        if n % div == 0:
            print(div)
        div = div + 1

print_divisors(20)


"""
#2. Define a function that, given as input 2 strings s1 and s2, 
returns a new string by appending s2 in the middle of s1. 
Print the output.
e.g. s1 = "Ault", s2 = "Kelly", output: "AuKellylt"
"""

def append_middle(s1, s2):
    middle_index = int(len(s1) / 2)
    print("input strings:", s1, s2)
    first_part = s1[:middle_index]
    second_part = s1[middle_index:]
    output = first_part + s2 + second_part
    return output

print(append_middle("Govind", "Ireland"))


"""
#3. Define a function that, given a string, arranges string characters 
such that lowercase letters should come first.
 e.g. heLLO --> heLLO
 e.g. HEllo --> lloHE
"""

def lower_first(s1):
    lower = []
    upper = []
    for char in s1:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    print(lower + upper)
    output = ''.join(lower + upper)
    return output

print(lower_first("goVINd"))


"""
#4. Define a function that, given a string as input, counts all lower case, uppercase, digits and special symbols. Print the output.
	e.g. ABC1234abcd,!j --> 5, 3, 4, 2
"""

def count_symbols(s):
    lower_cnt, upper_cnt, digit_cnt, spec_sym_cnt = 0, 0, 0, 0
    for char in s:
        if char.islower():
            lower_cnt = lower_cnt +1
        elif char.isupper():
            upper_cnt = upper_cnt + 1
        elif char.isnumeric():
            digit_cnt = digit_cnt + 1
        else:
            spec_sym_cnt = spec_sym_cnt + 1
    print("lower_cnt--", lower_cnt)
    print("upper_cnt--", upper_cnt)
    print("digit_cnt--", digit_cnt)
    print("spec_sym_cnt--", spec_sym_cnt)
    return lower_cnt, upper_cnt, digit_cnt, spec_sym_cnt


print(count_symbols("ABC1234abcd"))


"""
#5. Define a function that, given a string, 
checks how many numerals are present in the string.
 e.g. MScBIAS is the no 1 course in all 4 counties
 o/p = 2
"""

def get_numerics_from_string_approach2(str):
    res = 0
    for i in str:
        if(i.isdigit()):
            res += 1
    print(res)

get_numerics_from_string_approach2("MScBIAS is the no 123 course in all 446 counties")

"""
#6. Define a function such that, given a string, 
it should print all letters except "a" and "s".
	e.g. "MScBIAS"
	     o/p = McBI
"""
def print_letters_excluding_characters(str):
    stroutput = ""
    for letter in str:
        if letter == 'a' or letter == 's' or letter == 'A' or letter == 'S':
            continue
        stroutput += letter
    print(stroutput)
    
print_letters_excluding_characters("MScBIAS")


"""
#7. Write a program to accept a positive natural number (i.e., whole numbers excluding 0) from user. Pass this number as an argument to a function, which should print the sum of all numbers.
   from 1 to n 
   Hint: Use range()
"""
def print_sum_numbers(arg_number):
    sum_of_numbers = 0
    for i in range(1, arg_number):
        sum_of_numbers = sum_of_numbers + i
    print(sum_of_numbers)
    
user_number = int(input("Enter a number: "))
print_sum_numbers(user_number)






