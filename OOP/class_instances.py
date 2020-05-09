#creating class

class Student:
    
    def __init__(self,first,last,reg_no,branch):#__init__ is initialization , can be thought of as c++ constructor
        self.first = first
        self.last = last
        self.reg_no = reg_no
        self.branch =branch
    
    def fullname(self):
        return self.first+" "+self.last
#stud_1 , stud_2, stud_3 are class instances    
stud_1 = Student("Harsh","Gupta",170907514,"ECE")
stud_2 = Student("Karan","Sharma",170907422,"IT")
stud_3 = Student("Abhiroop","Razdhan",170807544,"Civil")

# Both the commands below will return same output    
print(stud_1.fullname())
print(Student.fullname(stud_1))
