import math


arrn=[413,317,332,405,5124,96,2]
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
def Radix_sort(arrn):
    v=max(arrn)
    arr=[0]*len(arrn)
    arrn1=arrn
    arrn1=arrn1[::-1]
    n=int(math.log10(v)+1)
    for j in range(n):
        print("Iteration ",j+1)
        arrn=arrn[::-1]
        for i in range(len(arrn)):
            arr[i]=arrn[i]%10
        print(arr)
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
        arr3=[0]*len(arr)
        for i in range(len(arr)):
            v=arr[i]
            val=arrn1[i]
            ind=arr2[v]-1
            arr2[v]=arr2[v]-1
            arr3[ind]=val
        print("sorted array : ",arr3)
        arrn=arr3
        arrn1=arrn[::-1]
        for i in range(j+1):
            for i in range (len(arrn)):
                arrn[i]=arrn[i]//10
        
        

Radix_sort(arrn)