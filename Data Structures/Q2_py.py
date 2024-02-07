arr=eval(input("Enter an array : "))
max_here=-99
max_so_far=-99
for i in range(len(arr)):
    max_here+=arr[i]
    if max_here<0:
        max_here=0
        
    if max_here>max_so_far:
        max_so_far=max_here
print(max_so_far)
        