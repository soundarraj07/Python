class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.last=None
    def create(self,value):
        n=node(value)
        self.addlist(n)
    def addlist(self,n):
        if self.head==None:
            self.head=n
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=n
            n.prev=temp
            self.last=n
    def delete_list(self,n,m):
        temp=self.head
        count=0
        while(temp.next!=None):
            i=0
            for i in range(n-1):
                if(temp.next!=None):
                    temp=temp.next
                else:
                    break
            t=temp
            if(t.next==None):
                break
            cnt=0
            for cnt in range (m+1):
                if temp.next!=None:
                    temp=temp.next
                else:
                    break
            t.next=temp
            temp.prev=t
    def print(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,"-->",end="")
            temp=temp.next
        temp=self.last
        print()
        while(temp!=None):
            print(temp.data,"-->",end="")
            temp=temp.prev
    
d=DLL()
d.create(110)
d.create(120)
d.create(130)
d.create(140)
d.create(150)
d.create(160)
d.create(170)
d.create(180)
d.create(190)
d.create(200)
d.create(210)
d.create(220)
d.create(230)
d.create(240)
d.create(250)

#n=int(input("enter the number of inputs you are going to give : "))
#for i in range (n):
 #   d.create(int(input()))
#m=int(input("Enter the M value :"))
#n=int(input("Enter the N value :"))
d.delete_list(3,2)
d.print()
