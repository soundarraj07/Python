m=int(input("Enter the value of m : "))
n=int(input("Enter the value of n : "))
arr=list()
print("Enter the elements : ")
for i in range(n):
    arr.append(int(input()))
i=0
for i in range(n):
    if (arr[i]+1==arr[i]):
        continue
    else:
        break
print("missing element is : ",arr[i]+1)