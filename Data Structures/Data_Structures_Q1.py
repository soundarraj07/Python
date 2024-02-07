n=int(input("Enter the N value : "))
print("Enter the integers : ")
arr=[]
for i in range (0,n):
    arr.append(int(input()))
for i in range (0,n):
    for j in range (0,n):
        if (arr[i]<arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in range (0,n-1):
    if arr[i]==arr[i+1]:
        print("Elements in an array should be distinct ")
        break
check=0
for i in range (0,n):
    if arr[i]+1==arr[i+1]:
        pass
    else:
        break
print(f'{arr[i]+1} is the missing element ')
