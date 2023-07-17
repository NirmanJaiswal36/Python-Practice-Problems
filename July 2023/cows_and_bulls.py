#source:https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
"""Create a program that will play the “cows and bulls” game with the user.
The game works like this:Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end."
"""

from random import *

num = randint(1000,9999)
guess = 0
count = 0
print(num,"")

def cow(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    cow = 0
    bull=0
    l1 = [int(x) for x in num1]
    l2 = [int(x) for x in num2]
    for element in l1:
        if element in l2:
            if element==l2[l1.index(element)]:
                cow+=1
            else:
                bull+=1
    print(cow," cows,",bull,"bulls")    

while guess!=num:
    count+=1
    guess = int(input("Enter any four-digit number here:"))
    cow(num,guess)

print("Number of games played:",count)