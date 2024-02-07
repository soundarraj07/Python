class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None 
class DLL:
    def __init__(self):
        self.head=None
        self.last=None
        self.n=int(input())
    def create(self,value):
        n=node(value)
        self.addlist(n)
    def addlist(self,n):
        if self.head==None:
            self.head=n
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=n
            n.prev=temp
            self.last=n
    def insert(self,data):
        temp=self.head
        if self.n==1:
            n=node(data)
            if temp.data>data:
                n.next=self.head
                self.head=n
            else:
                temp.next=n
        else:
            if (temp.data>data):
                n=node(data)
                n.next=temp
                self.head=n
            else:
                for i in range(self.n-1):
                    temp=temp.next
                if temp.data<data:
                    n=node(data)
                    temp.next=n
                else:

                    while(temp.next!=None):
                        if temp.data<=data:
                            temp=temp.next
                        else:
                            break
                    temp=temp.prev
                    n=node(data)
                    t=temp.next
                    temp.next=n
                    n.prev=temp
                    n.next=t
                    t.prev=n
    def print2(self):
        temp=self.head
        while(temp!=None):
            if temp.data==None:
                break
            print(temp.data,end=" ")
            temp=temp.next
            
        #temp=self.last
        #print()
        #while(temp!=None):
            #print(temp.data,"-->",end="")
            #temp=temp.prev
t=int(input())
d=[]
for i in range(t):
    d.append(DLL())
    for j in range(d[i].n):
        d[i].create(int(input()))
    data2=int(input())
    d[i].insert(data2)
i=0
for i in range(t):
    if (d[i].print2()!=None):
        print(d[i].print2(),end="")
    print()