row=int(input('Enter the no of rows '))
col=int(input('Enter the no of column'))
a=0
for i in range (0,row):
    for j in range (0,col):
        
        print(a%10,end=' ')
        a=a+1
    print()
