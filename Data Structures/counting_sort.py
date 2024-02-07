arr=[413,317,332,405,512,96,2]
def max(arr):
    max=arr[0]
    for i in range (len(arr)):
        if max<arr[i]:
            max=arr[i]
    return max
def freq(arr,value):
    count=0
    for i in range (len(arr)):
        if value==arr[i]:
            count+=1
    return count
def counting_sort(arr):
    arr1=[0]*(max(arr)+1)
    for i in range (len(arr1)):
        arr1[i]=freq(arr,i)
    print("step 1 : ",arr1)
    arr2=[0]*(max(arr)+1)
    i=1
    arr2[0]=arr1[0]
    for i in range(len(arr1)):
         arr2[i]=arr1[i]+arr2[i-1]
    print("step 2 : ",arr2)
    arr=arr[::-1]
    arr3=[0]*len(arr)
    for i in range(len(arr)):
        v=arr[i]
        ind=arr2[v]-1
        arr2[v]=arr2[v]-1
        arr3[ind]=v
    print("sorted array : ",arr3)
counting_sort(arr)