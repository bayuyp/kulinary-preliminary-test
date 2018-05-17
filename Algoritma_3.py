# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:43:21 2018

@author: bayuy
"""

# user input
N = 1345679

# cast input to string
str_N = str(N)

# trailing zeroes
trailing_zeroes = len(str_N) - 1

# for character in input
for i in str_N:
    # create string with character
    ans = ''
    ans += i
    # add zeroes from trailing zeroes
    for i in range(0, trailing_zeroes):
        ans += '0'
    # substract trailing zeroes
    trailing_zeroes -= 1
    # print answer
    print(ans)