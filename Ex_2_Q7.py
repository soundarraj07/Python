num=int(input("Enter the number 1 "))
num1=int(input("Enter the number 2 for GCD "))
if num1>num:
    sml=num
    lar=num1
else:
    sml=num1
    lar=num
while (True):
    rem=lar%sml
    lar=sml
    sml=rem
    if sml==0:
        break
print(f'Gcd is {lar}')
