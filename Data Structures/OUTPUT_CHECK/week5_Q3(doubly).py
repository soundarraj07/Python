class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.last=None
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
    def reverse(self,n,m):
        temp=self.head
        count=0
        while(temp.next!=None):
            temp=temp.next
            count+=1
            if count==n:
                a=temp
                break
        te=self.head
        temp=self.head
        count=0
        while(True):
            count+=1
            t=temp.next
            temp.next=temp.prev
            temp.prev=t
            if (count==n):
                if(temp!=None):
                    temp.prev=None
            if( count==n+1):
                break
            last=temp
            temp=t
        count=0
        temp=a
        while(True):
            count+=1
            t=temp.next
            temp.next=temp.prev
            temp.prev=t
            if (count==m):
                if(temp!=None):
                    temp.prev=None
            if( count==m+1):
                break
            last1=temp
            temp=t
        self.head.next=self.last
        self.last.prev=self.head
        self.head=last
        self.last=last1
        
    def print(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,"-->",end="")
            temp=temp.next
        print()
        temp=self.last
        while(temp!=None):
            print(temp.data,"-->",end="")
            temp=temp.prev
d=DLL()
n=int(input("enter the number of inputs you are going to give : "))
for i in range (n):
    d.create(int(input()))
d.reverse(3,2)
d.print()
