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
    def mid_element(self):
        temp=self.head
        temp2=self.head
        while(temp2.next):
            
            if (temp2.next.next):
                temp=temp.next
                temp2=temp2.next.next
            elif (temp2.next):
                temp2=temp2.next
            if(not temp2):
                break
        return temp.data
    def remove_duplicate(self):
        temp=self.head
        while(temp.next):
            temp2=temp.next
            temp3=temp
            while(temp2):
                if(temp.data==temp2.data):
                    if temp2.next is None:
                        temp3.next=None
                    temp3.next=temp2.next
                else:
                    temp3=temp2
                temp2=temp2.next
            temp=temp.next
            if temp==None:
                break
            
    def third_node_from_last(self):
        temp=self.head
        while(temp.next.next.next):
            temp=temp.next.next
            if not(temp or temp.next or temp.next.next):
                break
        return temp.data
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,"-->",end="")
            temp=temp.next
s=Singly_Linked_List()
s.create(1)
s.create(2)
s.create(3)
s.create(4)
s.create(5)
s.create(5)
s.create(5)
s.create(8)
s.create(1)
s.create(1)
s.create(1)
s.create(12)
s.create(12)
print("before removing duplicates")
s.display()
print("middle element is ",s.mid_element())
print("third node from last is ",s.third_node_from_last())
s.remove_duplicate()
print("after removing duplicates")
s.display()
