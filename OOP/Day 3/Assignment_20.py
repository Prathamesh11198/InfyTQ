#OOPR-Assgn-20
#Start writing your code here

class Applicant:
    __application_dict = {'A': 2, 'B': 3, 'C': 5}
    __applicant_id_count = 1000
    
    def __init__(self, applicant_name):
        self.__applicant_id = None
        self.__applicant_name = applicant_name
        self.__job_band = None
        
    def get_applicant_id(self):
        return self.__applicant_id
    
    def get_applicant_name(self):
        return self.__applicant_name
    
    def get_job_band(self):
        return self.__job_band
    
    @staticmethod
    def get_application_dict():
        return __application_dict
    
    def generate_applicant_id(self):
        self.__applicant_id=Applicant.__applicant_id_count + 1
        Applicant.__applicant_id_count += 1
        
    def apply_for_job(self, job_band):
        for key,value in Applicant.__application_dict.items():
            if key == job_band:
                if value < 5:
                    Applicant.__application_dict[key] += 1
                    self.generate_applicant_id()
                    self.__job_band=job_band
                else:
                    return -1
                    
                    
applicant1= Applicant("ABC")
applicant1.apply_for_job("A")
