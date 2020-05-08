# class methods and static methods
class Employee:
    
    raise_amt = 1.04 # raise_amt is class variable 
    num_of_emp = 0 
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emp +=1
    
    def fullname(self):
        return self.first+" "+self.last
    
    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    #class method
    @classmethod # decorator
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount  
    @classmethod
    def from_string(cls,emp_string):
        first,last,pay = emp_string.split('-')
        return cls(first,last,pay) # this will create a new employee object and assign values to first , last and pay
    
    @staticmethod # static method are not directly connected with class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

e1 = Employee('Harsh','Gupta',10000)
e2 = Employee('Karan','Sharma',9000)
Employee.set_raise_amt(1.05) #this will update the class variable 'raise_amt' to 1.05 instead of default 1.04

emp_info = 'Abhiroop-Razdhan-8500'
e3 = Employee.from_string(emp_info) # this will create a class instance and assign the values based on string passed.
print(e3.last) # returns Razdhan

# Static method work
##this not directly related to our class but might be needed
import datetime

my_date = datetime.date(2020,7,10)
print(Employee.is_workday(my_date))