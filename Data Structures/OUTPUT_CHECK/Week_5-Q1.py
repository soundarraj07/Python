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
    def delete_list(self,x,y):
        temp=self.head
        count=0
        while temp.next!=None:
            if count==0:
                x-=1
            elif count==1:
                x+=1
            for i in range (x):
                if temp.next!=None:
                    temp=temp.next
                else:
                    break
            temp0=temp
            for i in range (y):
                if temp.next!=None:
                    temp=temp.next
                else:
                    break
            temp0.next=temp.next
            count+=1
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
M=int(input("Enter M = "))
N=int(input("Enter N = "))
SLL.delete_list(M,N)
SLL.display()