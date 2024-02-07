class stack:
    def __init__(self):
        self.string=input()
        self.stack1=[]
        self.stack2=[]
        self.top2=-1
        self.top=-1
        self.check=0
    def push(self,data):
        self.check=1
        self.stack1.append(data)
    def pop1(self):
        self.check=0
        if self.stack1==[]:
            self.check+=1
        else:
            a=self.stack1.pop()
            return a
    def func(self):
        for i in range (len(self.string)):
            if self.string[i]=="[":
                self.push(self.string[i])
            elif self.string[i]=="{":
                self.push(self.string[i])
            elif self.string[i]=="(":
                self.push(self.string[i])
            elif self.string[i]==")":
                if "("==self.pop1():
                    self.check+=0
                else:
                    self.check+=1
            elif self.string[i]=="}":
                if "{"==self.pop1():
                    self.check+=0
                else:
                    self.check+=1
            elif self.string[i]=="]":
                if "["==self.pop1():
                    self.check+=0
                else:
                    self.check+=1
            else:
                self.check+=1
m=[]
n=int(input())
for i in range(n):
    m.append(stack())
    if (len(m[i].string)==1):
        m[i].check=1
        pass
    else:
        m[i].func()
for i in range(n):
    if (m[i].check==0 and len(m[i].string)!=1):
        print("YES")
    else:
        print("NO")


            
        


