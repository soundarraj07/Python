p=int(input('Enter the principal amount :')) 
i=int(input('Enter the Intereest :')) 
n=int(input('Enter the no. of years :'))
class Investment :
    def __init__(self,p,i,n): 
        self.pr=p
        self.i=i
        self.no=n 
        self.amount=0
def value_after(self) : 
    self.amount=self.pr*((1+self.i)**self.no)
def __str__(self) : 
    print('Principal :',self.pr) 
    print('Interest :',self.i) 
    print('Amount :',self.amount)
s1=Investment(p,i,n) 
s1.value_after() 
s1.__str__()