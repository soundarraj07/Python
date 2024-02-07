number=int(input("Enter the number "))
def sum_digits(num):
    sumu=0
    while (True):
        n=num%10
        num=int(num/10)
        sumu+=n
        if(num<=0):
            return sumu
            break 
ans=sum_digits(number)
print(ans)
