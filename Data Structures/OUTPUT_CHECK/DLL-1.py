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
    def delete_value_at_position(self,position):
        temp=self.head
        for i in range (position-2):
            temp=temp.next
        print(temp.data)
        add=temp
        temp=temp.next
        add.next=temp.next
        temp=temp.next
        temp.prev=add
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
        temp=n.next
        temp.prev=n
    def delete_last(self):
        temp=self.head
        while(temp.next!=None):
            add=temp
            temp=temp.next
        temp.prev=None
        add.next=None
    def delete_first(self):
        temp=self.head
        self.head=temp.next
        temp=temp.next
        temp.prev=None
    def delete(self,value):
        temp=self.head
        while(temp.next!=None):
            if (value==temp.data):
                add.next=temp.next
                temp=temp.next
                temp.prev=add
            add=temp
            temp=temp.next
    def display (self):
        temp=self.head
        print("first to last ")
        while(temp):
            print(temp.data,"-->",end=" ")
            temp=temp.next
        temp=self.head
        print()
        print("last to first ")
        while (temp.next!=None):
            temp=temp.next
        while(temp):
            print(temp.data,"-->",end=" ")
            temp=temp.prev
        temp=self.head
n=int(input("Enter the number of elements your going too create a doubly linked list : "))
s=DLL()
print("Enter the elemnts : ")
for i in range (n):
    m=int(input())
    s.create(m)
count=0
while(True):
    count+=1
    str=input("Enter function - delete last or delete value or insert value at position or delete value at position or add first or add last or delete first : ")
    if str=="add first":
        s.add_First(input("enter the element to add first "))
        s.display()
    elif count>=n:
        if(str=="delete last" or str=="delete first"):
            print("LIST IS EMPTY ")
    elif str=="delete last":
        s.delete_last()
        s.display()
    elif str=="delete value":
        s.delete(int(input("Enter the value to delete ")))
        s.display()
    elif str=="insert value at position":
        s.Insert_value(input("Enter the value "),int(input("enter the position ")))
        s.display()
    elif str=="delete value at position":
        s.delete_value_at_position(int(input("Enter the position ")))
        s.display()
    elif str=="insert middle":
        s.Insert_Middle(int(input("Enter the value to insert at middle position : ")))
        s.display()
    elif str=="delete first":
        s.delete_first()
        s.display()
    elif str=="add last":
        s.add_Last(int(input("Enter the value to add at last ")))
        s.display()
    elif str=="exit":
        break
    else:
        s.display()


          
            

