#Printing strings in triangle shape
n=input('Enter any string here:')
length=len(n)
for row in range(length):
    for col in range(row+1):
        print(n[col],end='')
    print('')    
    
    
