#015. Sum Square difference
#Source:https://projecteuler.net/problem=6
'''Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

def sum_of_squares(num1):
    sum=0
    for x in range(1, num1+1):
        sum += x*x
    return sum 

def square_of_sum(num2):
    sum=0
    for y in range(1,num2+1):
        sum += y
    sum = sum*sum
    return sum

def difference():
    a = int(input('Enter the number here, for which(how many numbers) you want to find the difference:'))
    diff = square_of_sum(a)-sum_of_squares(a)
    print('the difference between the sum of the squares of the first ', a , 'natural numbers and the square of the sum is ', diff)

difference()
