# special methods are surrounded by '__' and are also dunder/magic method.
# __init__ is a special method.
class Employee:
    
    raise_amt = 1.04 # raise_amt is class variable 

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def fullname(self):
        return self.first+" "+self.last
    
    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): # representation of class instance if you print class instatnce 
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
    
    def __str__(self): # this should be more readable for the end user.
        return '{}-{}'.format(self.fullname(),self.pay)
    # __repr__ and __str__ helps us to format how our object should be printed / represented

    def __add__(self,other): # this tells python class how to add two objects
        return self.pay + other.pay # in this case we are adding pay of of each employee
    
    def __len__(self): # len function
        return len(self.fullname())-1

e1 = Employee('Harsh','Gupta',10000)
e2 = Employee('Karan','Sharma',9500)

#print(e1+e2) # output is 19500 
print(len(e1))