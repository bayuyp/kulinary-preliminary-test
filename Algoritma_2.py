# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:12:41 2018

@author: bayuy
"""

# user input
N = 13

# list of  fibonacci 
fibonacci = []

# fill initial fibonacci numbers
fibonacci.append(0)
fibonacci.append(1)

# for number of input
for i in range(2, N):
    # create fibonacci number
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

# print fibonacci list
print(fibonacci)