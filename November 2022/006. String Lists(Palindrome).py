#006. String lists(Palindrome)
#Source:https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
'''Ask the user for a string and print out whether this string is a palindrome or not.'''

string = input('Enter anything here:')

x = len(string)
y=''

for a in range(-1,-x-1,-1):
    y = y + string[a]
    
if string==y:
    print('The input string is a palindrome')
else:
    print('It is not a palindrome')
