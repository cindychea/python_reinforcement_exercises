# In some countries of the former Soviet Union there was a belief about lucky tickets.
# A transport ticket of any sort was believed to possess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half.
# Here are examples of such numbers:
# 003111 # 3 = 1 + 1 + 1
# 813372 # 8 + 1 + 3 = 3 + 7 + 2
# 17935 # 1 + 7 = 3 + 5
# 56328116
# Your task is to write a method luckCheck(str), which returns true if argument is string decimal representation of a lucky ticket number, or false for all other numbers. 
# It should handle errors for empty strings or strings which don't represent a decimal number

import math


def luck_check(string):
    if string == '' or int(string) < 0:
        print('Not a valid string')
    else:
        upper = math.ceil(len(string) / 2)
        lower = math.floor(len(string) / 2)
        sum = 0
        for i in range(0, lower):
            sum += int(string[i])
        sum1 = 0
        for i in range(upper, len(string)):
            sum1 += int(string[i])
        if sum == sum1:
            print(True)
        else:
            print(False)


luck_check('003111')
luck_check('813372')
luck_check('913371')
luck_check('17935')
luck_check('56328116')
luck_check('')
luck_check('-003111')
