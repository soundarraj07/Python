import random
a=100
while(True):
    inp=input('Enter you guessing Hint: Head or tail : ')
    b=random.randint(0,1)
    if b==0:
        inp1='tail'
    elif b==1:
        inp1='head'
    if inp==inp1:
        a+=9
        print('You won')
    else :
        a-=10
        print('You lost')
    print(a)
