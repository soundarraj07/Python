class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class CSLL:
    def __init__(self):
        self.head=None
    def create(self,value):
        n=node(value)
        self.addlist(n)
    def addlist(self,n):
        if(self.head==None):
            self.head=n
            n.next=self.head
        else:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=n
            n.next=self.head
    def insert_middle(self,value):
        n=node(value)
        temp=self.head
        count=0
        while(temp.next!=self.head):
            count+=1
            temp.temp.next
        temp=self.head
        for i in range (count//2-1):
            temp=temp.next
        n.next=temp.next
        temp.next=n
    def add_first(self,value):
        n=node(value)
        temp=self.head
        n.next=temp
        while(temp.next!=self.head):
            temp=temp.next
        temp.next=n
        self.head=n
    def add_last(self,value):
        n=node(value)
        temp=self.head
        while(temp.next is not self.head):
            temp=temp.next
        temp.next=n
        n.next=self.head
    def delete_first(self):
        temp=self.head
        self.head=temp.next
        temp=self.head
        while(temp.next != self.head):
            temp=temp.next
        temp.next=self.head
    def display (self):
        temp=self.head
        while (True):
            print(temp.data,"--›",end=" ")
            temp=temp.next
            if temp==self.head:
                break
s=CSLL()
s.create(10)
s.create(20)
s.create(30)
s.create(40)
#s.add_first(1)
#s.add_last(2)
s.delete_first()
s.display()
