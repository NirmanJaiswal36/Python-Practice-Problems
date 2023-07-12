# generates a random number and takes user input and compares the two.

from random import *
i = randint(1,10)

number = int(input("Enter any number here:\n"))

while number!=i:
    if number>i:
        print("Greater")
        number = int(input("Enter another number:\n"))
    elif number<i:
        print("Smaller")
        number = int(input("Enter another number:\n"))
    else:
        break

print("The number you entered,i.e, ",number," is guessed correct")
