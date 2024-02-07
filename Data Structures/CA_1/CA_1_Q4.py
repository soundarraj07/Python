class array:
    def __init__(self):
        self.length=int(input())
        self.arr=eval(input())
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
if len(a.arr)>a.length or len(a.arr)<a.length:
            print("Invalid input ")
else:
    a.functions()
    print(a.spanarr)
