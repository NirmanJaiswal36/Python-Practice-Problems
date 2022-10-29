#004. Odd or Even
#Source:https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

'''
Question: Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.

'''

number = int(input("Enter any number here:"))

if number%2==0:
    print("The number you entered is even")
else:
    print("The number you entered is odd.")


'''
Extras: Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''

num = int(input("Enter the divsor:"))
check = int(input("Enter the dividend here:"))

if check%num==0:
    print('The dividend is divisible by the divisor')
else:
    print('The dividend is not divisible by the divisor')
