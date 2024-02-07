lst=[]
for i in range (0,7):
    a=int(input('Enter the number : '))
    lst.append(a)
sum=0
c=0
count=0
cou=0
for i in range (0,7):
    sum+=lst[i]
    if lst[i]>0:
        c+=1
    if lst[i]<0:
        count+=1
    if lst[i]==0:
        cou+=1
print(f'Sum is {sum}')
print(f'no of positive {c}')
print(f'no of negative is {count}')
print(f'no of zeros is {cou}')