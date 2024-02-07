arr=list()
a=list()
n=int(input("Enter the size of an integer array your going to give : "))
print("Enter the array of integers : ")
for i in range (n):
    arr.append(int(input()))
i=0
x=int(input("Enter the input X value : "))
for i in range (n):
    for j in range(n):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)
i=0
c=0
sum=arr[i]
for i in range(n):
    print(type(arr[i]),type(x))
    print(arr[i],">",x)
    print(arr[i]>x)
    sum+=arr[i+1]
    if(arr[i]>x==True):
        print("The smallest sub array is : ",'[',arr[i],']')
        break
    elif(sum>x):
        c=1
        index=i
        break       
        
i=0
if(c==1):
    a=arr[i:index+2:1]
    print("The smallest sub array the sum is greater than the x value is ,,: ",a)



        
