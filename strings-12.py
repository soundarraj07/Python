strn=input('Enter the string ')
strng=''
for i in range (0,len(strn)):
    
    if i%2!=0:
        strng+=strn[i].upper()
    else :
        strng+=strn[i]
print(strng)
