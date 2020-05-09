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
    
class Developers(Employee): # we created a new class which inherits from Employee class
    raise_amt = 1.10 # if a Developers instance is created then the raise will be 10% i.e. it overides the Employee Class raise_amt
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) #this will let the super class i.e. Employee in this case, __init__ to handle first,last and pay 
        self.prog_lang = prog_lang # and prog_lang can be added though this line of code.
        #Employee.__init__(self,first,last,pay) ## this can also be used instead of super.

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is  None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        print(self.fullname())
        for emp in self.employees:
            print('->',emp.fullname())

e1 = Employee('Harsh','Gupta',10000)
e2 = Employee('Karan','Sharma',9000)
d1 = Developers('HC','Verma',100000,"Physics")
d2 = Developers('Abdul','Bari',100000,"DSA")
m1 = Manager('Jose','Mourinho',10500,[e1,e2])

m1.print_emp()