import random


while(True) :
    a=int(input('Enter 0 for Rock , 1 for paper , 2 for scissors , 3 for EXIT GAME : '))
    b=random.randint(0,2)
    print(f'I choosen {b}')
    if a==b:
        print('Its Draw 😇')
    elif a==0 and b==1:
        print('I won 😎')
    elif a==0 and b==2:
        print('You won 😡')
    elif a==1 and b==0:
        print('You won 🥲')
    elif a==1 and b==2:
        print('I won 🤣')
    elif a==2 and b==0:
        print('I won 😎')
    elif a==2 and b==1:
        print('You won 😡')
    elif a==3:
        break
