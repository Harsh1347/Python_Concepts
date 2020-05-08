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

e1 = Employee('Harsh','Gupta',10000)
print(e1.pay)
e1.pay_raise()
print(e1.pay)

# class variable value can be changed using following line of code
Employee.raise_amt = 1.05 # this will change the raise amount for all the class instances i.e. this is class variable
e1.raise_amt = 1.05 # this will change the raise amount only for e1 class instances i.e. this is instance variable
