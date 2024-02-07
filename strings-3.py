strn=input('Enter the formula :')
c1=0
c2=0
for i in range (0,len(strn)):
    if strn[i]=='{' :
        c1+=1
    if strn[i]=='}':
        c2+=1
if c1==c2 :
    print(" The formula has enough peranthesis ")
else :
    print("The formula does not have enough peranthesis ")
