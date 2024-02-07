strings=list(eval(input("Enter the array of srtings")))
lst=[]
def add_excietment(lst):
    for i in range (0,len(lst)):
        lst[i]=lst[i]+'!'
    return lst
lst=add_excietment(strings)
print(lst)

        
