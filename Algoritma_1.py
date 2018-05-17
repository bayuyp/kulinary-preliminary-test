# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:22:56 2018

@author: bayuy
"""

# user input
N = 25

# list of prime numbers
prime = []

# fill number 2
prime.append(2)

# iteration of number
num = 3
# get first N prime numbers
while len(prime) <= N-1:
    flag = True
    # check if number is prime
    for i in range(3, num, 2):
        if num % i == 0:
            flag = False
            break
    # if prime add to list
    if flag == True:
        prime.append(num)
    num += 2

print(prime)