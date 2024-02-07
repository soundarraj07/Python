a=int(input("Enter the no of rows : "))
b=int(input("Enter the no of columns : "))
def Rectangle(m,n):
    for i in range (0,m):
        for j in range (0,n):
            print('*')
        print()
Rectangle(a,b)