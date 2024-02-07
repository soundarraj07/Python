class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def create(self,value):
        n=node(value)
        self.addlist(n)
    def addlist(self,n):
        if(self.head==None):
            self.head=n
        else:
            temp=self.head
            while(temp.next!=None):
                print("kk")
                temp=temp.next
            temp.next=n
    
    def insert(self,value,position):
        n=node(value)
        temp=self.head
        for i in range (position-2):
            print("c")
            temp=temp.next
        n.next=temp.next
        temp.next=n
    def insert_Middle(self,value):
        count=1
        n=node(value)
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
            count=count+1
        temp=self.head
        for i in range ((count//2)-1):
            temp=temp.next
        
        n.next=temp.next
        temp.next=n
        
    
    def delete(self,position):
        temp=self.head
        for i in range(position-2):
            temp=temp.next
        add=temp
        temp=temp.next
        add.next=temp.next
    def delete_value(self,value):
        temp=self.head
        count=0
        g=1
        while(temp.next is not None):
            g=g+1
            temp=temp.next
        temp=self.head
        for j in range(g):
            print(temp.data,"==",value)
            count=count+1
            if(temp.data==value):
                
                if(count==1):
                    self.head=temp.next
                else:ad.next=temp.next
            ad=temp
            temp=temp.next  
    def insert(self,value,position):
        n=node(value)
        temp=self.head
        for i in range (position-2):
            print("c")
            temp=temp.next
        n.next=temp.next
        temp.next=n    
    def display (self):
        temp=self.head
        while (temp):
            print(temp.data,"--›",end=" ")
            temp=temp.next
    


s1=SLL()
s1.create(100)
s1.create(4)
s1.create(9)
s1.create(76)
s1.create(2)
s1.create(56)
s1.create(100)
s1.insert_Middle(400)
s1.insert(2,2)
s1.delete_value(100)

s1.display()


