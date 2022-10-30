#003. Character Input
#Source:https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Note: for this exercise,the expectation is that you explicitly write out the year (and therefore be out of date the next year).
"""

name = input("Enter your name here:")
age = int(input("Enter your age here:"))
year = 2022

print("Dear "+name+",you will turn hundred years old in the year "+ str(year-age+100))

num = int(input("Enter the number of times you want to see the message:"))

print(num * ("Dear "+name+",you will turn hundred years old in the year "+ str(year-age+100)+'\n'))


