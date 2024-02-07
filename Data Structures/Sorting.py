def Bubble_sort(arr):
    for i in range(len(arr)):
        check=0
        for j in range (len(arr)-1-i):
            if (arr[j]>arr[j+1]):
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
                check=1
        if check==0:
            break
    return arr
def Selection_sort(arr):
    index=0
    for i in range(len(arr)):
        min=arr[i]
        check=0
        for j in range(len(arr)-i):
            if min>arr[j+i]:
                min=arr[j+i]
                index=j+i
                check=1
        if check==1:
            temp=arr[i]
            arr[i]=min
            arr[index]=temp
    return arr
def Selection_sort2(arr):#wrong
    index=0
    j=0
    for i in range(len(arr)):
        min=arr[i]
        check=0
        j+=i
        while(arr[j]<min):
                min=arr[j]
                index=j
                check=1
                j+=1
        if check==1:
            temp=arr[i]
            arr[i]=min
            arr[index]=temp
    return arr
      
arr=[62,41,33,30,69,9,288,44]
print(Bubble_sort(arr))
print(Selection_sort2(arr))