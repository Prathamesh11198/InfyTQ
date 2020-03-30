#OOPR-Assgn-7
#Start writing your code here

class Instructor:
    def __init__(self):
        self.__instructor_name = None
        self.__technology_skill = []
        self.__experience = None
        self.__avg_feedback = None
        
    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name
        
    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill
    
    def set_experience(self, experience):
        self.__experience = experience
        
    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback
        
    def get_instructor_name(self):
        return self.__instructor_name
        
    def get_technology_skill(self):
        return self.__technology_skill
    
    def get_experience(self):
        return self.__experience
        
    def get_avg_feedback(self):
        return self.__avg_feedback
        
    def check_eligibility(self):
        if(self.__experience > 3 and self.__avg_feedback >= 4.5):
            return True
        elif(self.__experience <= 3 and self.__avg_feedback >= 4):
            return True
        else:
            return False
            
    def allocate_course(self, technology):
        if technology in self.__technology_skill:
            if self.check_eligibility():
                self.__technology_skill.append(technology)
                return True
            else:
                return False
        else:
            return False
        
I1 = Instructor()
I1.set_instructor_name("ABC")
I1.set_technology_skill(["ML", "AI"])
I1.set_experience(5)
I1.set_avg_feedback(4.8)

print(I1.allocate_course("Data science"))