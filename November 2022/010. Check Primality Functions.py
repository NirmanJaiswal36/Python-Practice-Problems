#010. Check Primality functions
#Source:https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
'''Ask the user for a number and determine whether the number is prime or not.'''

def division(num):
    x = range(2,num)
    y = [num%x for x  in x]
    if 0 in y:
        print('The number is not prime.')
    else:
        print('It is a prime number.')

a = int(input('Enter any number here:'))
division(a)
