class stack:
    def __init__(self):
        self.num=int(input())
        self.inp=eval(input())
        self.input2=eval(input())
        self.top=-1
        self.top2=-1
        self.min=999
        self.min2=0
        self.minindex=0
        self.stack1=[]
        self.stack2=[]
        self.min3=[]
    def push1(self,data):
        self.stack1.append(data)
        self.top+=1
    def push2(self,data):
        self.stack2.append(data)
        self.top2+=1
    def peak(self):
        return self.stack1[self.top]
    def pop1(self):
        if self.top==-1:
            return -1
        a=self.stack1[self.top]
        self.stack1.pop()
        self.top-=1
        return a
    def operations(self):
        for i in range (len(self.inp)):
            if (self.inp[i]=="stack"):
                pass
            elif (self.inp[i]=="push"):
                if self.min>self.input2[i]:
                    self.min=self.input2[i]
                    self.min3.append(self.min)
                self.push1(self.input2[i])
            elif (self.inp[i]=="pop"):
                if (self.peak()==self.min3[len(self.min3)-1] and (self.min3)):
                    self.min3.pop()
                if(not(self.min3)):
                    self.min=999
                self.push2(self.pop1())
            elif (self.inp[i]=="peak"):
                self.push2(self.peak())
            elif(self.inp[i]=="minval"):
                self.push2(self.min3.pop())            
s=stack()
s.operations()
#print(s.stack1)
#print(s.minindex)
print(s.stack2)
