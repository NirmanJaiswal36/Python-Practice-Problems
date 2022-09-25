#Floyd Pattern
n=int(input('Enter number of rows here:'))
num=1
for row in range(1,n+1):
    for col in range(row):
        print(num, end=' ')
        num=num+1
    print('')    
