class Stack:
    def __init__(self):
        self.arr=[None]*15
        self.arr2=[None]*15
        self.top=-1
        self.top2=-1
        self.input1=[]
        self.input2=[]
        self.n=0
        self.track=0
    def receiver(self):
        self.n=int(input())
        if self.n>15:
            print("operations should not exceed 15 ")
        else:
            self.input1=eval(input())
            self.input2=eval(input())
        self.arr=[None]*self.n
        self.arr=[None]*self.n
    def push(self,value):
        if (self.top==self.n):
            print("Stack is full ! ")
        else:
            self.top+=1
            self.arr[self.top]=value
    def push2(self,value):
        if (self.top2==self.n):
            print("Stack is full ! ")
        else:
            self.top2+=1
            self.arr2[self.top2]=value
    def operations(self):
        count=0
        for i in range(self.n):
            if (self.input1[i]=="BrowserHistory"):
                self.push(None)
                self.push2(self.input2[i])
            elif (self.input1[i]=="visit"):
                self.push(None)
                self.push2(self.input2[i])
            elif (self.input1[i]=="back"):
                count+=1
                if count==1:
                    self.track=self.top2
                num=self.input2[i]
                self.track=self.track-num
                self.push(self.arr2[self.track])
            elif (self.input1[i]=="forward"):
                num=self.input2[i]
                self.track+=num
                self.push(self.arr2[self.track])
s=Stack()
s.receiver()
s.operations()
print(s.arr)
print(s.arr2)


    