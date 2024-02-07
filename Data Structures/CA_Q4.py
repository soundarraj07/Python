class array:
    def __init__(self):
        self.length=int(input())
        self.arr=eval(input("Enter the array : "))
        self.spanarr=[]
    def functions(self):
        for i in range (len(self.arr)):
            span=1
            for j in range(i):
                if self.arr[i]>=self.arr[j]:
                    span+=1
                else:
                    span=1
            self.spanarr.append(span)
a=array()
a.functions()
print(a.spanarr)



    