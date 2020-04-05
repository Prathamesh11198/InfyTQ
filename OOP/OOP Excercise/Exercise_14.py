#OOPR-Tryout
#Start writing your code here

class InvalidMechanicIdException(Exception):
    pass

class InvalidMechanicSpecializationException(Exception):
    pass

class VehicleService:
    def __init__(self, mechanic_list):
        self.__mechanic_list = mechanic_list
    
    def assign_vehicle_for_service(self, mechanic_id, vehicle_type):
        flag = 0
        for mech in self.__mechanic_list:
            if mechanic_id == mech.get_mechanic_id():
                flag = 1
                if vehicle_type == mech.get_specilization():
                    mech.set_vehicle_count(mech.get_vehicle_count()+1)
                else:
                    raise InvalidMechanicSpecializationException("Invalid Specilization")
        
        if flag == 0:
            raise InvalidMechanicIdException("Invalid Mechanic ID")

class Mechanic:
    def __init__(self, mechanic_id, specilization, vehicle_count):
        self.__mechanic_id = mechanic_id
        self.__specilization = specilization
        self.__vehicle_count = vehicle_count
        
    def set_mechanic_id(self, mechanic_id):
        self.__mechanic_id = mechanic_id
        
    def set_specilization(self, specilization):
        self.__specilization = specilization
        
    def set_vehicle_count(self, vehicle_count):
        self.__vehicle_count = vehicle_count
        
    def get_mechanic_id(self):
        return self.__mechanic_id
        
    def set_specilization(self):
        return self.__specilization
    
    def set_vehicle_count(self):
        return self.__vehicle_count
        
try:
    m1 = Mechanic(101, "TW", 1)
    lst = []
    lst.append(m1)
    vs = VehicleService(lst)
    vs.assign_vehicle_for_service(102, "TW")
    
except  InvalidMechanicIdException as e:
    print(str(e))
    
except InvalidMechanicSpecializationException as e:
    print(str(e))
    

    
        