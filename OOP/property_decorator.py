
class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
       
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return self.first+' '+self.last

    @fullname.setter # setter property
    def fullname(self,name):
        first,last = name.split(' ')
        self.first =first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('deleted')

e1 = Employee('Harsh','Gupta') 
print(e1.last)
e1.fullname = 'Harsh Guptamorya' #setter function is used to change the name everywhere. without setter this would'nt be possible
print(e1.last)

del e1.fullname # this would use deleter and delete the full name

