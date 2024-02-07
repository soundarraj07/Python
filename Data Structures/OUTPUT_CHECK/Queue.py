class queue:
    def __init__(self):
        self.front=-1
        self.rear=-1
        self.arr=[None]*5
    def enqueue(self,value):
        if self.rear+1==5:
            print("Queue is full ")
        else:
            if self.front==-1:
                self.front+=1
                self.rear+=1
            else:
                self.rear+=1
            self.arr[self.rear]=value
    def dequeue(self):
        if self.front==-1:
            print("Queue is empty ")
        else:
            a=self.arr[self.front]
            self.arr[self.front]=None
            self.front+=1
            return a
s=queue()
while(True):
    str=input("Enter what you need to do : ")
    if str=='enqueue':
        s.enqueue(input("Enter the element : "))
        print(s.arr)
    elif str=='dequeue':
        print(s.dequeue())
        print(s.arr)
    elif str=='exit':
        break
        
