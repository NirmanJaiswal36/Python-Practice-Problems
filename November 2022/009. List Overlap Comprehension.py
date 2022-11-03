#009. List Overlap Comprehension
#Source:https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
'''Randomly generate two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this using at least one list comprehension.'''

from random import*

a = sample(range(100), randint(1,15))
b = sample(range(100), randint(1,15))
print(a)
print(b)

c = [element for element in a if element in b]
d = [*set(c)]
print(d)


   
