n=int(input("Enter the N value : "))
print("Enter the integers : ")
arr=[]
check=0
for i in range (0,n):
    arr.append(int(input()))
for i in range (0,n):
    for j in range(i+1,n-1):
        
        index=j
        if arr[i]==arr[j+1]:
            check=1
            break
        
        else:
            continue
    if check==1:
        break
print(f'{index+1} is the first repeating index ')
