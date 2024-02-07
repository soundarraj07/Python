n=int(input("Enter the length of array : "))
arr=[]
arr1=[]
for i in range (3):
    for j in range(3):
        arr1.append(int(input()))
    print(arr1)
    arr.append(arr1)
    arr1=[]
arr2=[0]*n
for i in range(3):
    sind=arr[i][0]
    sind=sind-1
    eind=arr[i][1]
    eind=eind-1
    
    val=arr[i][2]
    while sind<=eind:
        arr2[sind]+=val
        sind+=1
print(arr2)