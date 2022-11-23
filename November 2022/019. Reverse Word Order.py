#019. Reverse Word Order
#Source:https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
'''Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.'''

string = input('Enter a long string:')
result = string.split()
reverse = ''
rev_list = []
a = len(result)

for x in range(-1,-a-1,-1):
    reverse= reverse+result[x]+' '
    rev_list.append(result[x])

rev_list = " ".join(rev_list)
print(reverse)
print(rev_list)




    
