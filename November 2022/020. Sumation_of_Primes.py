#019. Summation of Primes
#Source:https://projecteuler.net/problem=10
'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.'''

import time

start = time.time()
'''x=2
total = 0

while x<2000000:
    y = range(2,int(x**0.5)+1)
    remainder = [x%element for element in y ]
    if 0 not in remainder:
        total += x
    x+=1    
    
print(total)'''

total = 17
for x in range(11,2000000):
    for y in range(2,int(x**0.5)+1):
        if x%y==0:
            break
    else:
        total+=x
 
print(total)        
end = time.time()
print('The time taken to run the program is',end-start,"s")
