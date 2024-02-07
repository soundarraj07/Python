class Queue_using_stack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.output=[]
        self.n=int(input())
        self.inp1=eval(input())
        if (self.n>(len(self.inp1))) or (self.n<(len(self.inp1))):
            print("Error : Enter valid number of operation ")
        self.inp2=eval(input())
        if (self.n>(len(self.inp2))) or (self.n<(len(self.inp2))):
            print("Error : Enter the valid number of inputs ")
    def push1(self,value):
        self.stack1.append(value)
    def pop1(self):
        return self.stack1.pop()
    def push2(self,value):
        self.stack2.append(value)
    def pop2(self):
        return self.stack2.pop()
    def peak(self):
        return self.stack1[len(self.stack1)-1]
    def empty(self):
        if (not self.stack1):
            return True
        else:
            return False
    def Queue(self):
        for i in range (len(self.inp1)):
            if (self.inp1[i]=="push"):
                count=0
                while(len(self.stack1)!=0):
                    count+=1
                    self.push2(self.pop1())
                    if(len(self.stack1)==0):
                        break
                self.push1(self.inp2[i])
                while(len(self.stack2)!=0):
                    self.push1(self.pop2())
            elif (self.inp1[i]=="pop"):
                if self.stack1==[]:
                    self.output.append(-1)
                else:
                    self.output.append(self.pop1())
            elif (self.inp1[i]=="peak"):
                if self.stack1==[]:
                    self.output.append(-1)
                else:
                    self.output.append(self.peak())
            elif (self.inp1[i]=="Queue"):
                pass
            else:
                break
q=Queue_using_stack()
if (q.n>(len(q.inp1))) or (q.n>(len(q.inp2))) or (q.n<(len(q.inp2))) or (q.n<(len(q.inp1))):
    pass
else:
    q.Queue()
    print(q.output)
                
