class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singly_Linked_List:
    def __init__(self):
        self.head=None
    def create(self,value):
        n=node(value)
        self.addlist(n)
    def addlist(self,n):
        if self.head==None:
            self.head=n
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=n
    def traversal(self):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        return temp
    def add_first(self,value):
        if self.head==None:
            self.create(value)
        else:
            n=node(value)
            n.next=self.head
            self.head=n
    def add_Last(self,value):
        n=node(self)
        temp=self.traversal()
        temp.next=n
    def insert_middle(self,value):
        temp=self.head
        n=node(value)
        count=0
        while(temp.next!=None):
            temp=temp.next
            count+=1
        temp=self.head
        for i in range (count//2 - 1):
            temp=temp.next
        n.next=temp.next
        temp.next=n
    def delete_last(self):
        temp=self.head
        while(temp.next!=None):
            add=temp
            temp=temp.next
        add.next=None
    def delete_first(self):
        temp=self.head
        self.head=temp.next
        temp.next=none
    def delete_value(self,value):
        temp=self.head
        while(temp.next!=None):
            if (temp.data==value):
                add.next
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
n=int(input("Enter the number of elements your going to add to singly linked list : "))
SLL=Singly_Linked_List()
print("Enter the elemnts : ")
for i in range (n):
    m=int(input())
    SLL.create(m)

SLL.create(6)
SLL.create(7)
SLL.delete_last()
SLL.display()

