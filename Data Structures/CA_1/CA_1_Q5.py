n=int(input())
arr=eval(input())
low=0
high=len(arr)-1
def min_in_rotated_sorted(arr,low,high):
    while(low<high):
        mid=((low+high)//2)
        if (mid==0 or arr[mid-1]>arr[mid] ):
            return arr[mid]
        elif(arr[mid+1]<arr[mid]):
            return arr[mid+1]
        if (arr[mid]>arr[high]):
            low=mid+1
        elif (arr[mid]<arr[low]):
            high=mid-1
        else:
            return arr[0]
    return -1
if n>len(arr) or n<len(arr):
    print("Enter the valid input ")
else:
    print(min_in_rotated_sorted(arr,low,high))