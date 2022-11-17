#018. Special Pythagorean Triplet
#Source:https://projecteuler.net/problem=9
'''There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.'''

'''combinations = [(i,j,1000-i-j) for i in range(1,999) for j in range(1,1000-i)]'''

for i in range(1,999):
    for j in range(1,1000-i):
        k = 1000-i-j
        if i*i + j*j == k*k and i<j:
            print('The required pythagorean triplet is',i,j,k)
            print('And the product is', i*j*k)
            
       
            
        

            
