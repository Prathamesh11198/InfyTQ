#OOPR-Exer-6
#Start writing your code here
                                                    

class Vehicle:
    def __init__(self):
        self.mileage = None
        self.fuel_left = None
        
    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left - 5 > 0:
            dist = (self.fuel_left-5)*self.mileage
            return dist
        else:
            return 0
            
    def identify_distance_travelled(self, initial_fuel):
        remain_fuel = initial_fuel - self.fuel_left
        dist = remain_fuel * self.mileage
        return dist
        
    
car1 = Vehicle()
car1.mileage = 25
car1.fuel_left = 10
print(car1.identify_distance_travelled(15))
print(car1.identify_distance_that_can_be_travelled())