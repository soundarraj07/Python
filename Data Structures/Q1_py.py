arr=eval(input("Enter an array : "))
for i in range (len(arr)):
    for j in range (len(arr)-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
for i in range (len(arr)-1):
    if (arr[i]+1!=arr[i+1]):
        print(arr[i]+1)
        break
