class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.last=None
        self.head2=None
        self.last2=None
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
    def create2(self,value):
        n=node(value)
        self.addlist2(n)
    def addlist2(self,n):
        if self.head2==None:
            self.head2=n
        else:
            temp=self.head2
            while(temp.next!=None):
                temp=temp.next
            temp.next=n
            n.prev=temp
            self.last2=n
    def linker(self,n):
        temp=self.head
        temp1=self.head2
        while(temp!=None):
            temp0=temp.next
            temp.next=temp1
            temp1.prev=temp
            temp2=temp1.next
            temp1.next=temp0
            temp=temp0
            temp1=temp2
            if temp0==None:
                break
            temp0.prev=temp1
            
        self.head2=temp1
        

    def print(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,"-->",end="")
            temp=temp.next
        temp=self.last
        print()
        #while(temp!=None):
            #print(temp.data,"-->",end="")
            #temp=temp.prev
        temp=self.head2
        print()
        while(temp!=None):
            print(temp.data,"-->",end="")
            temp=temp.next
        temp=self.last2
        print()
        #while(temp!=None):
            #print(temp.data,"-->",end="")
            #temp=temp.prev
d=DLL()
n=int(input("enter the number of inputs you are going to give : "))
for i in range (n):
    d.create(int(input()))
n=int(input("enter the number of inputs you are going to give : "))
for i in range (n):
    d.create2(int(input()))
d.linker(n)
d.print()
    