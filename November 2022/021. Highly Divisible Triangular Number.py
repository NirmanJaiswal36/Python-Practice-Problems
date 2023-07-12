#021. Highly Divisible Triangular Number
#Source:https://projecteuler.net/problem=12
'''What is the value of the first triangle number to have over five hundred divisors?'''


def tri_num(num):
    s = 0
    for x in range(1,num+1):
        s += x
    return s

def divisors(num):
    x = range(1,num+1)
    y = [element for element in x if num%element==0]
    z = len(y)
    return z

num_of_divisors=0
num=1
while num_of_divisors<=501:
    number = tri_num(num)
    num_of_divisors = divisors(number)
    num+=1
    
print(number)
    
