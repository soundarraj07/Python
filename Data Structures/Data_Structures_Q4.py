n=int(input("Enter the N value : "))
print("Enter the integers : ")
arr=[]
check=0
for i in range (0,n):
    arr.append(int(input()))
for i in range (1,n):
    if (arr[i-1]<arr[i]>arr[i+1]):
        index=i
        check=1
        break
if check==0:
    print("Peak element does not exist")
else:
    print(f'The peak element index is {index} and the element is {arr[index]}')
