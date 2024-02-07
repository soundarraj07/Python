class alexa:
    def __init__(self):
        self.str=input()
        self.inp=list(map(int,self.str.split()))
        self.key=self.inp[2]
        self.str1=input()
        self.str2=input()
        self.inp1=list(map(int,self.str1.split()))
        self.inp2=list(map(int,self.str2.split()))
        self.stack1=self.inp1[::-1]
        self.stack2=self.inp2[::-1]
        self.count=0
    def pop1(self):
        return self.stack1.pop()
    def push1(self,value):
        self.stack1.append(value)
    def pop2(self):
        return self.stack2.pop()
    def push2(self,value):
        self.stack2.append(value)
    def game(self):
        c=-1
        while(True):
            c+=1
            if(c==len(self.inp2)or c==len(self.inp1)):
                break
            elif(self.pop1()+self.pop2()<=self.key):
                self.count+=2
            
            else:
                break
n=int(input())
a=[]
for i in range(n):
    a.append(alexa())
    a[i].game()
for i in range(n):
    print(a[i].count)

