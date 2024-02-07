
strng=input("Enter strng : ")
n=len(strng)
print(f'a.number of letters are : {n}')
print(f'c.the first string : {strng[0]}')
print(f'd.the first three string : {strng[0:3:]}')
print(f'e.the last three string : {strng[-3::]}')
print(f'h.the first letter and last letter is removed : {strng[1:n-1:]}')
if n>6:
    print(f'g.the 7 th letter is : {strng[6]}')
else :
    print('The string does not have sufficient characters to print')
print(f'f.The reverse of the string is : {strng[-1::-1]}')
print(f'The string in capoital letter {strng.upper()}')
strn=''
for i in range (0,n):
    if (strng[i]!='a'):
        strn+=strng[i]
    else :
        strn+='e'
print(f' a replaced by e {strn}')


