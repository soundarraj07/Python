class stack:
    def __init__(self):
        self.top=-1
        self.arr=[None]*10
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
def value(x):
    if x=='+' or x=='-':
        return 1
    elif x=='*' or x=='/':
        return 2
    elif x=='^':
        return 3
    else:
        return 0
inp=input("enter the infix notation :")
for i in range (len(inp)):
    if inp[i].isalnum():
        print(inp[i],end="")
    else:
        if inp[i]=='(':
            s.push(inp[i])
        elif inp[i]==')':
            while(s.arr[s.top]!='(' and s.top!=-1):
                print(s.pop(),end="")
            s.pop()  
        elif (value(s.arr[s.top]))<=(value(inp[i])):
            s.push(inp[i])
        elif (value(s.arr[s.top]))>=(value(inp[i])):
            while(True):
                if (value(s.arr[s.top]))>=(value(inp[i])):
                    print(s.pop(),end="")
                else:
                    break
            s.push(inp[i])
        
while(s.arr[s.top]!=None):
    print(s.pop(),end="")
        
