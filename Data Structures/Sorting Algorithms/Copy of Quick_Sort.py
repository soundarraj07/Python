#Quick_Sort
arr=[34,61,54,45,76,23,12]
def Quick_Sort(arr,start,end):
    i=start-1
    j=start
    pivot=end
    if start >= pivot :
        return 
    while(j<=pivot):
        if arr[pivot] > arr[j]:
            i+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        j+=1
    temp = arr[pivot]
    i+=1
    arr[pivot]=arr[i]
    arr[i]=temp
    pivot=i
    Quick_Sort(arr,start,pivot-1)
    Quick_Sort(arr,pivot+1,end)
Quick_Sort(arr,0,len(arr)-1)
print(arr)
        
        