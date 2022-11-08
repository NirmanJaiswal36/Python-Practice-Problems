#011. Fibonacci
#Source:https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions.'''

def fibonacci(num):
    y=1
    x=1
    print(x,y, end=' ')
    for a in range(num-2):
        b = x+y
        print(b, end=' ')
        x=y
        y=b

num = int(input('Enter the number of fibonacci numbers you want:'))
fibonacci(num)
