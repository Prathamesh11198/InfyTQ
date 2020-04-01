#OOPR-Assgn-30
#Start writing your code here

types=['small', 'medium']

class Customer:
    def __init__(self, customer_name, quantity):
        self.__customer_name = customer_name.lower()
        self.__quantity = quantity
        
    def validate_quantity(self):
        if self.__quantity in range(1,6):
            return True
        else: 
            return False
            
    def get_customer_name(self):
        return self.__customer_name
        
    def get_quantity(self):
        return self.__quantity
    
    
class Pizzaservice:
    counter = 100
    
    def __init__(self, customer, pizza_type, additional_topping):
        self.__customer = customer
        self.__pizza_type = pizza_type
        self.__additional_topping = additional_topping
        self.pizza_cost = 0
        self.__service_id=None
        
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in types:
            return True
        else:
            return False
            
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            if self.__pizza_type.lower() == "small" :
                self.pizza_cost = 150 * self.__customer.get_quantity()
                if self.__additional_topping:
                    self.pizza_cost += 35 * self.__customer.get_quantity()
                    
            if self.__pizza_type.lower() == "medium":
                self.pizza_cost = 200 * self.__customer.get_quantity()
                if self.__additional_topping:
                    self.pizza_cost += 50 * self.__customer.get_quantity()
                    
            if not self.__service_id:
                self.__service_id = self.__pizza_type[0] + str(Pizzaservice.counter+1)
                Pizzaservice.counter+=1
        else:
            self.pizza_cost=-1
            
    def get_service_id(self):
        return self.__service_id
        
    def get_pizza_type(self):
        return self.__pizza_type
    
    def get_customer(self):
        return self.__customer
    
    def get_additional_topping(self):
        return self.__additional_topping


class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        self.__delivery_charge = 0
        self.__distance_in_kms = distance_in_kms
        super().__init__(customer, pizza_type, additional_topping)
        
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False
            
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                
                if self.__distance_in_kms <= 5:
                    self.pizza_cost += self.__distance_in_kms*5
                elif self.__distance_in_kms in range(6, 11):
                    self.pizza_cost += 25+(self.__distance_in_kms-5)*7
        else:
            self.pizza_cost = -1
            
    def get_delivery_charge(self):
        return self.__delivery_charge
    
    def get_distance_in_kms(self):
        return self.__distance_in_kms


cust1 = Customer("ABC", 3)
d = Doordelivery(cust1, "Small", False, 10)
d.calculate_pizza_cost()
print(d.pizza_cost)
print(d.get_service_id())