inp=input("enter the reverse polish notation to evaluvate : ")
class stack:
    def __init__(self):
        self.top=-1
        self.arr=[]
    def push(self,val):
        if self.top==10:
            print("Stack is full")
        else:
            self.top+=1
            self.arr[self.top]=val
    def pop(self):
        if self.top==-1:
            print("stack is empty")
        else:
            a=self.arr[self.top]
            self.arr[self.top]=None
            self.top-=1
            return a
s=stack()
for i in range (len(inp)):
    if inp[i].isnumeric():
        s.push(int(inp[i]))
    else:
        if inp[i]=='*':
            a=s.pop()
            b=s.pop()
            s.push(a*b)
        elif inp[i]=='+':
            a=s.pop()
            b=s.pop()
            s.push(a+b)
        elif inp[i]=='-':
            a=s.pop()
            b=s.pop()
            s.push(a-b)
        elif inp[i]=='^':
            a=s.pop()
            b=s.pop()
            s.push(a^b)
        elif inp[i]=='/':
            a=s.pop()
            b=s.pop()
            s.push(a//b)
print(s.arr[0])
        
        
    
