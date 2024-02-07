string=input('Enter the string : ')
count=0
for i in range (0,len(string)):
    if (string[i].isspace()):
        pass
    else :
        count+=1
print('The number ofr wordes in the string is : ',count)
