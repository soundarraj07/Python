num=int(input('Enter the number : '))
i=2
flag=0
while(num > i*i):
    if num%(i*i) == 0:
        flag=1
    else :
        flag+=0
    i+=1
if flag==1:
    print('It is not sqaure free number')
else:
    print('It is square free number ')
    
