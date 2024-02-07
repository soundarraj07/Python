class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def create(self,value):
        n=node(value)
        self.addlist(n)
    def addlist(self,n):
        
        if self.head==None:
            self.head=n
            n.prev=None
        else:
            temp=self.head
            while(temp.next!=None):
                print("kk")
                temp=temp.next
            temp.next=n
            n.prev=temp
    def Insert_value(self,value,position):
        n=node(value)
        temp=self.head
        for i in range (position-2):
            temp=temp.next
        n.next=temp.next
        temp.next=n
        n.prev=temp
        temp=temp.next
        temp=temp.next
        temp.prev=n  
    def add_First(self,value):
        n=node(value)
        temp=self.head
        n.next=temp
        temp.prev=n
        self.head=n
    def add_Last(self,value):
        n=node(value)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=n
        n.prev=temp
    def Insert_Middle(self,value):
        count=1
        temp=self.head
        n=node(value)
        while(temp.next!=None):
            temp=temp.next
            count=count+1
        temp=self.head
        for i in range((count//2)-1):
            temp=temp.next
        n.next=temp.next
        n.prev=temp
        temp.next=n
        temp=temp.next
        temp=temp.next
        temp.prev=n
    def delete(self,value):
        temp=self.head
        count=0
        c=1
        p=0
        while(temp.next is not None):
            c=c+1
            if(temp.data==value):
                p=p+1
            temp=temp.next
            
        temp=self.head
        print(p)
        for j in range (c-p):
            
            count=count+1
            
            if (temp.data==value):
                
                if(count==1):
                    self.head=temp.next
                    temp=temp.next
                    temp.prev=None
                else:
                    add.next=temp.next
                    temp=temp.next
                    temp.prev=add
            add=temp
            temp=temp.next
    def display (self):
        temp=self.head
        while (temp.next!=None):
            temp=temp.next
        while(temp):
            print(temp.data,"-->",end=" ")
            temp=temp.prev
        temp=self.head
        print()
        while(temp):
            print(temp.data,"-->",end=" ")
            temp=temp.next
s=DLL()
s.create(10)
s.create(20)

s.create(30)
#s.create(10)
s.create(40)
s.create(50)

s.Insert_value(25,3)
s.add_First(100)
#s.add_Last(1)
s.Insert_Middle(100)
s.delete(100)
s.display()
            
            
