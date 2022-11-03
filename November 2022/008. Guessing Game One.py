#008. Guessing Game One
#Source: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.'''

from random import*
num="Yes"
game_num = 0
x = randint(1,9)

while num!="Exit" or num=="exit":
    game_num +=1
    num = input('Take a guess about the number(1 to 9) or press Exit:')
    y = int(num)
    if y>x:
        print('too high')
    elif y<x:
        print('too low')
    else:
        print('You guessed the right number, i.e.', x)
        print('No. of games:',game_num)
        break
        
    
    
