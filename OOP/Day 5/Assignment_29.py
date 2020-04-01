#OOPR-Assgn-29
#Start writing your code here

from abc import ABCMeta, abstractmethod

class Customer(metaclass=ABCMeta):
    def __init__(self,customer_name):
        self.bill_id = 0
        self.__customer_name = customer_name.title()
        self.bill_amount = 0
        
    @abstractmethod
    def calculate_bill_amount(self):
        pass
    
    def get_customer_name(self):
        return self.__customer_name


class OccasionalCustomer(Customer):
    __counter=1000
    
    def __init__(self, customer_name, distance_in_kms):
        self.__distance_in_kms = distance_in_kms
        super().__init__(customer_name)
        self.bill_id = "O"+str(OccasionalCustomer.__counter+1)
        OccasionalCustomer.__counter+=1
        
    def validate_distance_in_kms(self):
        if self.__distance_in_kms>=1 and self.__distance_in_kms<=5:
            return True
        else:
            return False
            
    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            tiffin_cost = 50
            distance = 1
            if self.__distance_in_kms <= 2:
                self.bill_amount = self.__distance_in_kms * 5
            elif self.__distance_in_kms in range(3, 6):
                    self.bill_amount = (self.__distance_in_kms)*7.5
                    
            self.bill_amount += tiffin_cost
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount
            
    def get_distance_in_kms(self):
        return self.__distance_in_kms
        
        
class RegularCustomer(Customer):
    __counter=100
    
    def __init__(self, customer_name, no_of_tiffin):
        self.__no_of_tiffin = no_of_tiffin
        super().__init__(customer_name)
        self.bill_id = "R"+str(RegularCustomer.__counter+1)
        RegularCustomer.__counter += 1
        
    def validate_no_of_tiffin(self):
        if self.__no_of_tiffin in range(1,8):
            return True
        else:
            return False
            
    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            tiffin_cost = 50
            self.bill_amount = tiffin_cost*self.__no_of_tiffin*7
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount
            
    def get_no_of_tiffin(self):
        return self.__no_of_tiffin
        
c1 = OccasionalCustomer("ABC", 3)
print(c1.calculate_bill_amount())