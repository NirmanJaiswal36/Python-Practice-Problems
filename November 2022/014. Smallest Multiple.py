#014. Smallest Multiple
#Source:https://projecteuler.net/problem=5
'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

x = range(1,21)
prime = [2,3,5,7,11,13,17,19]

num = 20
condition = 'true'
while condition == 'true':
    y = [num%element for element in x]
    z = set(y)
    if len(z)==1:
        print('The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is',
              num)
        condition = 'false'
    else:
        num +=20
        condition = 'true'
        
    


