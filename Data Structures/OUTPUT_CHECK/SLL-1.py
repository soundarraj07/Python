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
        temp.next=None
    def delete_value(self,value):
        temp=self.head
        while(temp.next!=None):
            if (temp.data==value):
                add1.next=temp.next
            add1=temp
            temp=temp.next
    def insert_value_at_position(self,value,position):
        n=node(value)
        temp=self.head
        for i in range (position-2):
            temp=temp.next
        n.next=temp.next
        temp.next=n
    def delete_value_at_position(self,position):
        temp=self.head
        for i in range (position-2):
            temp=temp.next
        temp.next=temp.next.next
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
n=int(input("Enter the number of elements your going too create a singly linked list : "))
SLL=Singly_Linked_List()
print("Enter the elemnts : ")
for i in range (n):
    m=int(input())
    SLL.create(m)
count=0
while(True):
    count+=1
    
    str=input("Enter function - delete last or delete value or insert value at position or delete value at position or add first or add last or delete first : ")
    if str=="add first":
        SLL.add_first(int(input("enter the element to add first ")))
        SLL.display()
    elif count>=n:
        if(str=="delete last" or str=="delete first"):
            print("LIST IS EMPTY ")
    elif str=="delete last":
        SLL.delete_last()
        SLL.display()
    elif str=="delete value":
        SLL.delete_value(2)
        SLL.display()
    elif str=="insert value at position":
        SLL.insert_value_at_position(int(input("Enter the value ")),int(input("enter the position ")))
        SLL.display()
    elif str=="delete value at position":
        SLL.delete_value_at_position(int(input("Enter the position ")))
        SLL.display()
    elif str=="insert middle":
        SLL.insert_middle(int(input("Emter the value to insert at middle position : ")))
        SLL.display()
    elif str=="delete first":
        SLL.delete_first()
        SLL.display()
    elif str=="add last":
        SLL.add_Last(int(input("Enter the value to add at last ")))
        SLL.display()
    elif str=="exit":
        break
    else:
        SLL.display()

