#016. 1001st Prime Number
#Source:https://projecteuler.net/problem=7
'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?'''

prime = []
a = len(prime)
x=2
while a<10001:
    y = range(2,x)
    z = [x%element for element in y]
    if 0 not in z:
        prime.append(x)
    x += 1
    a = len(prime)


print(prime[10000])    
    
