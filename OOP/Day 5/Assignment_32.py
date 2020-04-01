#OOPR-Assgn-32
#Start writing your code here
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self, employee_name, qualification, job_band, basic_salary):
        self.__employee_name = employee_name
        self.__qualification = qualification
        self.__job_band = job_band
        self.__basic_salary = basic_salary
        
    def get_employee_name(self):
        return self.__employee_name
        
    def get_qualification(self):
        return self.__qualification
        
    def get_job_band(self):
        return self.__job_band
        
    def get_basic_salary(self):
        return self.__basic_salary
        
    def validate_basic_salary(self):
        if self.__basic_salary > 3000:
            return True
        else:
            return False
            
    def validate_qualification(self):
        if self.__qualification in ["Bachelors", "Masters"]:
            return True
        else:
            return False
            
    @abstractmethod
    def validate_job_band(self):
        pass
    
    @abstractmethod
    def calculate_gross_salary(self):
        pass
    
class Graduate(Employee):
    def __init__(self, employee_name, qualification, job_band, basic_salary, cgpa):
        super().__init__(employee_name, qualification, job_band, basic_salary)
        self.__cgpa = cgpa 
        
    def get_cgpa(self):
        return self.__cgpa
        
    def validate_job_band(self):
        if self.get_job_band() in ["A", "B", "C"]:
            return True
        else:
            return False
            
    def calculate_gross_salary(self):
        if self.validate_job_band() and self.validate_qualification() and self.validate_basic_salary():
            pf = self.get_basic_salary()*0.12
            
            if self.get_job_band() == "A":
                jb = 0.04
            elif self.get_job_band() == "B":
                jb = 0.06
            elif self.get_job_band() == "C":
                jb = 0.10
                
            jb = self.get_basic_salary()*jb
            
            if self.__cgpa >= 4 and self.__cgpa <= 4.25:
                cgp = 1000
            elif self.__cgpa >= 4.26 and self.__cgpa <= 4.5:
                cgp = 1700
            elif self.__cgpa >= 4.51 and self.__cgpa <= 4.75:
                cgp = 3200
            elif self.__cgpa >= 4.76 and self.__cgpa <= 5.0:
                cgp = 5000
                
            gross_salary = self.get_basic_salary() +pf + jb + cgp
            return gross_salary
        else:
            return -1
            
    
class Lateral(Employee):
    def __init__(self, employee_name, qualification, job_band, basic_salary, skill_set):
        super().__init__(employee_name, qualification, job_band, basic_salary)
        self.__skill_set = skill_set 
        
    def get_skill_set(self):
        return self.__skill_set
        
    def validate_job_band(self):
        if self.get_job_band() in ["D", "E", "F"]:
            return True
        else:
            return False
            
    def calculate_gross_salary(self):
        if self.validate_job_band() and self.validate_qualification() and self.validate_basic_salary():
            pf = self.get_basic_salary()*0.12
            
            if self.get_job_band() == "D":
                jb = 0.13
            elif self.get_job_band() == "E":
                jb = 0.16
            elif self.get_job_band() == "F":
                jb = 0.20
                
            jb = self.get_basic_salary()*jb
            
            if self.__skill_set == "AGP":
                sk = 6500
            elif self.__skill_set == "AGPT":
                sk = 8200
            elif self.__skill_set == "AGDEV":
                sk = 11500
                
            gross_salary = self.get_basic_salary() +pf + jb + sk
            return gross_salary
        else:
            return -1
            

grad = Lateral("Sarah", "Masters", "D", 6500, "AGP")
print(grad.calculate_gross_salary())
    
        
    