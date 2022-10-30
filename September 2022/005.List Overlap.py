#005.List Overlap
#Source:https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
''' Question: Randomly generate two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).'''

from random import*

a = []
b = []

for x in range(randint(5,10)):
    a.append(randint(0,100))
for y in range(randint(5,10)):
    b.append(randint(0,100))
print(a)
print(b)

c = a + b
d = []

for element in c:
    if element not in d:
        d.append(element)        

print(d)        
