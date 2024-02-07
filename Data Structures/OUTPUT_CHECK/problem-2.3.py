class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.count=0
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
    def delete_from_last(self,position):
        temp=self.head
        for i in range (position-2):
            temp=temp.next
        add=temp
        temp=temp.next
        add.next=temp.next
    def delete_first(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
n=int(input("Enter the length of your list :"))
c=SLL()
for i in range(n):
    c.create(int(input()))
c.print()
print()
gvn=int(input("Enter the position you needto delete from last : "))
if gvn<n:
    p=n-gvn+1
    c.delete_from_last(p)
    c.print()
elif gvn==n:
    c.delete_first()
    c.print()
else:
    print("Invalid Input")


