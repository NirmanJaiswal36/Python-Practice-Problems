#012. Largest Prime Factor
#Source:https://projecteuler.net/problem=3
'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

import math


prime_factor = []
num = int(input('Enter the number whose largest prime factor you want:'))
x = range(2,num//2)


factors = [a for a in x if num%a==0]

for factor in factors:
    y = range(2,factor)
    rem = [factor%element for element in y]
    if 0 not in rem:
        prime_factor.append(factor)

print(max(prime_factor))

