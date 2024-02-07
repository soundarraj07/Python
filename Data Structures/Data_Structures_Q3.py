arr=list()
n=int(input("Enter the size of an array :  "))
print("Enter the array of integers in 0s ,1s ,2s : ")
for i in range (0,n):
    arr.append(int(input()))
temp=0
for i in range (0,n):
    for j in range (0,n):
        if (arr[i]<arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        
print(arr)
