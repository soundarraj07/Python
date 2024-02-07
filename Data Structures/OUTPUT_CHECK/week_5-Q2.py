class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singly_Linked_List:
    def __init__(self):
        self.head1=None
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
    def create1(self,value):
        n=node(value)
        self.addlist1(n)
    def addlist1(self,n):
        if self.head1==None:
            self.head1=n
        else:
            temp=self.head1
            while temp.next!=None:
                temp=temp.next
            temp.next=n
    def linker(self):
        temp=self.head
        temp1=self.head1
        temp0=self.head
        while(temp!=None):
            temp2=temp.next
            temp.next=temp1   
            temp0=temp1.next
            temp1.next=temp2
            temp=temp.next
            temp=temp.next
            temp1=temp0
        self.head1=temp0
            
            
    def display(self):
        print("List 1 : ")
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
        print("\nList 2: ")
        temp=self.head1
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
n=int(input("Enter the number of elements your going to create a singly linked list : "))
SLL=Singly_Linked_List()
print(" Enter the elemnts : ")
for i in range (n):
    m=int(input())
    SLL.create(m)
n1=int(input("Enter the number of elements your going to create another singly linked list : "))
print(" Enter the elemnts : ")
for i in range (n1):
    m=int(input())
    SLL.create1(m)
SLL.linker()
SLL.display()
    