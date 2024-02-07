arr=[34,61,54,45,16,23,12]
def insertion_sort(arr):
    for i in range(len(arr)-1):
        j=i+1
        while(arr[j-1]>arr[j]):
            temp=arr[j]
            arr[j]=arr[j-1]
            arr[j-1]=temp
            j=j-1
            if j==0:
                break
insertion_sort(arr)
print(arr)
            