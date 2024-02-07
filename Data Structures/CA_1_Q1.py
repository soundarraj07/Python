class stack:
    def __init__(self):
        self.inp=eval(input("Enter the array of operations :"))
        self.input2=eval(input("Enter the array of elements :"))
        self.top=-1
        self.top2=-1
        self.min=999
        self.min2=0
        self.minindex=0
        self.stack1=[]
        self.stack2=[]
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
                if self.min not in self.stack1:
                    self.min=self.input2[i]
                elif self.min>self.input2[i]:
                    self.min2=self.min
                    self.min=self.input2[i] 
                self.push1(self.input2[i])
            elif (self.inp[i]=="pop"):
                if self.inp[i]==self.min:
                    self.min=self.min2
                self.push2(self.pop1())
            elif (self.inp[i]=="peak"):
                self.push2(self.peak())
            elif(self.inp[i]=="minval"):
                self.push2(self.min)            
s=stack()
s.operations()
print(s.stack1)
print(s.minindex)
print(s.stack2)