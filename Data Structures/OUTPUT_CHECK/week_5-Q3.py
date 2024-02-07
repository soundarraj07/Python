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
    def reverse_list(self,l):
        temp=self.head
        prev=None
        count=0
        while(temp!=None):
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
            count+=1
            if count==l:
                break
        self.head=prev
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
n=int(input("Enter the number of elements your going to create a singly linked list : "))
SLL=Singly_Linked_List()
print(" Enter the elemnts : ")
for i in range (n):
    m=int(input())
    SLL.create(m)
SLL.reverse_list(3)
SLL.display()