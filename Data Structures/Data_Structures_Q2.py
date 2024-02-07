arr=list()
n=int(input("enter the size of your input array :"))
print("Enter the array of distinct integers  : ")
for i in range (0,n):
    arr.append(int(input()))
k=int(input("Enter the K value : "))
if (k>n):
    print("K value should not exceed size of an array : ")
check=0
for i in range (0,n):
    for j in range (0,n):
        if (arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in range (0,n-1):
    if arr[i]==arr[i+1]:
        print("Elements in an array should be distinct ")
        break
print(f'{arr[k-1]} is the {k}th largest number ')


