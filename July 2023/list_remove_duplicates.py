#source:https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.(also using sets)

a = [1,2,3,8,4,3,4,5,8]
b = []

for element in a:
    if element not in b:
        b.append(element)

print(b)


#using set

a = set(a)
a = list(a)
print(a)