def merge(arr, low, high):
    mid = low + (high - low) // 2
    left = []
    right = []
    for i in range(low, mid + 1):
        left.append(arr[i])
    for i in range(mid + 1, high + 1):
        right.append(arr[i])
    i = 0
    j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return

def merge_sort(arr, low, high):
    if low == high:
        return
    mid = low + (high - low) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, high)
    if low == 0 and high == len(arr) - 1:
        return arr
    return

def string(arr):
    ans = ''
    for i in arr:
        ans += i
    return ans

col, row = [int(i) for i in input().split()][ :2]
inputs = []
for _ in range(row):
    input1 = str(input())
    inputs.append(list(input1))

hashmap = []
for i in range(row):
    sorted_row = merge_sort([_ for _ in inputs[i]], 0, col - 1)
    unsorted_row = inputs[i]
    mismatch = 0
    for char in range(col):
        if sorted_row[char] != unsorted_row[char]:
            mismatch += 1
    hashmap.append((i, mismatch))

hashmap.sort(key = lambda x : x[1])
for ans in hashmap:
    print(string(inputs[ans[0]]))
