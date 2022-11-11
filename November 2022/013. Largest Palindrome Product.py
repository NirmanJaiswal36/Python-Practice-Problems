#013. Largest Palindrome Product
#Sourcehttps://projecteuler.net/problem=4
'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''


palindrome = []
string = ''
for x in range(100,1000):
    for y in range(100,1000):
        a = x*y
        num = str(a)
        b = len(num)
        for c in range(-1,-b-1,-1):
            string = string + num[c]
            if string == num:
                palindrome.append(int(string))
        string= ''        
                

print('The largest palindrome product made from two 3-digit numbers is', max(palindrome))

        
        
        
