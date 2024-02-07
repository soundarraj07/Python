class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singly_Linked_List:
    def __init__(self):
        self.head=None
        self.arr=[]
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
    def critical_finder(self):
        temp=self.head
        while(temp.next.next!=None):
            if(temp.data>temp.next.data and temp.next.data<temp.next.next.data):
                self.arr.append(temp.next)
            temp=temp.next
    def maxdistance(self):
        if (len(self.arr)<2):
            return -1
        temp=self.arr[0]
        count=0
        while(temp!=self.arr[len(self.arr)-1]):
            count+=1
            temp=temp.next
        return count
    def mindistance(self):
        if (len(self.arr)<2):
            return -1
        distance=[]
        for i in range(len(self.arr)-1):
            temp=self.arr[i]
            count=0
            while(temp!=self.arr[i+1]):
                count+=1
                temp=temp.next
            distance.append(count)
        return min(distance)

arr1=[]
s=Singly_Linked_List()
arr2=eval(input())
for i in range(len(arr2)):
    s.create(arr2[i])
s.critical_finder()
#for i in range(len(s.arr)):   //to print critical points
    #print(s.arr[i].data,end=" ")
arr1.append(s.mindistance())
arr1.append(s.maxdistance())
print(arr1)



