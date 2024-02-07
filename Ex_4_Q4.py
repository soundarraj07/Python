num=int(input("Enter the number :"))

def digital_root (nom):
    while(nom>9):
        sum=0
        while(nom):
            n=nom%10
            nom//=10
            sum+=n
        nom=sum
    return nom
ans=digital_root(num)
print(ans)
            
