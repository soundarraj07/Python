class stack:
    def __init__(self):
        self.inp=int(input())
        self.input1=eval(input("Enter the operations : "))
        self.input2=eval(input("Enter the webpages : "))
        self.stack1=[]
        self.top=-1
        self.top2=-1
        self.stack2=[]
        self.output=[]
    def push1(self,homepage):
        self.stack1.append(homepage)
        self.top+=1
    def peak(self):
        return self.stack1[self.top]
    def browserhistory(self,homepage):
        self.push1(homepage)
        self.output.append(None)
    def visit(self,url):
        self.push1(url)
        self.top=len(self.stack1)-1
        self.output.append(None)
        while(not(self.stack2==[])):
            self.stack2.pop()
    def back(self,n):
        for i in range(n):
            if(self.top==0):
                break
            self.stack2.append(self.stack1.pop())
            self.top-=1  
            if(self.stack1==[]):
                break
        self.output.append(self.peak())
    def forward(self,n):
        for i in range (n):
            if (self.stack2==[]):
                break
            self.push1(self.stack2.pop())
        self.output.append(self.peak())
    def operations(self):
        for i in range(self.inp):
            if self.input1[i]=="BrowserHistory":
                self.browserhistory(self.input2[i])
            elif self.input1[i]=="back":
                self.back(self.input2[i])
            elif self.input1[i]=="visit":
                self.visit(self.input2[i])
            elif self.input1[i]=="forward":
                self.forward(self.input2[i])
s=stack()
s.operations()
print(s.top)
print(s.output)


        
