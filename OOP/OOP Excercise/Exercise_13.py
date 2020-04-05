#OOPR-Exer-13
#Start writing your code here
from abc import ABCMeta, abstractmethod

class DirectToHomeService(metaclass = ABCMeta):
    __counter = 100
    
    def __init__(self, consumer_name):
        self.__consumer_name = consumer_name
        self.__consumer_number = DirectToHomeService.__counter
        DirectToHomeService.__counter += 1
        
    def get_consumer_name(self):
        return self.__consumer_name
        
    def get_consumer_number(self):
        return self.__consumer_number
        
    @abstractmethod
    def calculate_monthly_rent(self):
        pass
    
class BasePackage(DirectToHomeService):
    def __init__(self, base_pack_name, subscription_period, consumer_name):
        super().__init__(consumer_name)
        self.__base_pack_name = base_pack_name
        self.__subscription_period = subscription_period
        
    def get_base_pack_name(self):
        return self.__base_pack_name
    
    def get_subscription_period(self):
        return self.__subscription_period
        
    def validate_base_pack_name(self):
        if self.__base_pack_name not in ["Silver", "Gold", "Platinum"]:
            self.__base_pack_name = "Silver"
            print("Base package name is incorrect, set to Silver")
        
        return True
    
    def calculate_monthly_rent(self):
        discount = 0
        if self.__subscription_period in range(1, 25):
            if self.validate_base_pack_name():
                if self.__base_pack_name == "Silver":
                    if self.__subscription_period > 12:
                        discount = 350
                    rent = 350
                elif self.__base_pack_name == "Gold":
                    if self.__subscription_period > 12:
                        discount = 440
                    rent = 440
                elif self.__base_pack_name == "Platinum":
                    if self.__subscription_period > 12:
                        discount = 560
                    rent = 560
                    
                final_rent = ((rent*self.__subscription_period) - discount)/self.__subscription_period
                return final_rent
        else:
            return -1
        

cust1 = BasePackage("silver", 24, "ABC")
print(cust1.calculate_monthly_rent())
    
    
    
        
        
        
        
        
        