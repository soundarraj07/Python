num=56
for i in range (0,10):
    num1=int(input('Enter the number you guessed : '))
    diff=abs(num-num1)
    if num<num1:
        print('higher ')
        if diff>10:
            print('Much higher ')
        
    if num1<num:
        print('lower ')
        if diff<10:
            print("Much lower ")
