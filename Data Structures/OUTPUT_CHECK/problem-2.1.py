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
    
    def swap(self,n):
        if n>=2:
            temp0=self.head
            temp1=self.head.next
            temp0.next=temp1.next
            temp1.next=self.head
            temp=self.head
            self.head=temp1
            
            if n>3:
                i=2
                while(i<n-1):
                    temp0=temp.next
                    temp1=temp0.next
                    temp.next=temp1
                    temp0.next=temp1.next
                    temp1.next=temp0
                    temp=temp0
                    i+=2

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
    
s=Singly_Linked_List()
#s.create(10)
#s.create(20)
#s.create(30)
#s.create(40)
#s.create(50)
#s.create(40)
#s.create(5)
#s.create(7)
n=int(input("Enter how many inputs you are going to enter : "))
print("Enter input one by one : ")
for i in range (n):
    s.create(int(input()))
s.display()
print()
s.swap(n)
print("After swap : ")
print()
s.display()