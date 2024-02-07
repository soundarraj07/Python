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
    def solution(self,x):
        temp=self.head
        head=self.head
        while(True):
            temp=temp.next
            if temp.data==x :
                print(temp.data)
                break
        while(temp.next != None):
            modifier=self.head
            mod2=self.head.next
            temp0=temp
            temp1=temp.next
            temp=temp.next
            if  temp.data<x:
                modifier.next=temp0.next
                add=temp.next
                temp0.next=add
                temp1.next=mod2
                self.head=temp1
            temp=temp.next
            
        self.head=head
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
        #i=0
        #for i in range (6):
            #print(temp.data,"-->",end=" ")
            #temp=temp.next
s=Singly_Linked_List()
n=int(input("Enter how many inputs you are going to enter : "))
print("Enter input one by one : ")
for i in range (n):
    s.create(int(input()))
x=int(input("Enter the input x : "))
#s.create(1)
#s.create(4)
#s.create(3)
#s.create(2)
#s.create(5)
#s.create(2)
#s.solution(3)

s.solution(x)
s.display()

