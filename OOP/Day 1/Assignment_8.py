#OOPR-Assgn-8
#Start writing your code here
class Student:
   
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        
    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False
            
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
            
    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.__marks>=65:
                return True
        return False
        
    def set_student_id(self, student_id):
        self.__student_id = student_id
        
    def get_student_id(self):
        return self.__student_id
        
    def set_marks(self, marks):
        self.__marks=marks
        
    def get_marks(self):
        return self.__marks
        
    def set_age(self, age):
        self.__age=age
        
    def get_age(self):
        return self.__age
        
s1=Student()
s1.set_student_id(1)
print(s1.get_student_id())
s1.set_age(21)
print(s1.get_age())
s1.set_marks(66)
print(s1.get_marks())
s1.check_qualification()