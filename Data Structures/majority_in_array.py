arr=[]
n=int(input("Enter the size of an array : "))
print("Enter the elements of array : ")
for i in range (n):
    arr.append(input())
i=0
c=0
check=0
for i in range (n):
    c=0
    for j in range (n):
        if(arr[i]==arr[j]):
            c=c+1
    
    if(n//2<c):
        print("Majority Element is :",arr[i])
        break
    else:
        check=1
if(check==1):
    print("No majority elements in an array ")