#OOPR-Assgn-11
#Start writing your code here

flower_list = ["Orchid","Rose", "Jasmine"]
level_list = [15, 25, 40]

class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None
        
    def validate_flower(self):
        if self.__flower_name in flower_list:
            return True
        else:
            return False
            
    def validate_stock(self, required_quantity):
        if required_quantity > self.__stock_available:
            return False
        else:
            return True
            
    def sell_flower(self, required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available -= required_quantity
            
    def check_level(self):
        if self.validate_flower():
            flower_level=level_list[flower_list.index(self.__flower_name)]
            if self.__stock_available < flower_level:
                return True
        return False
        
    def get_flower_name(self):
        return self.__flower_name
        
    def get_price_per_kg(self):
        return self.__price_per_kg
        
    def get_stock_available(self):
        return self.__stock_available
    
    def set_flower_name(self, flower_name):
        self.__flower_name=flower_name.title()
        
    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg
        
    def set_stock_available(self, stock_available):
        self.__stock_available=stock_available
        
a=Flower()
a.set_flower_name('Jasmine')
a.set_price_per_kg(300)
a.set_stock_available(35)
print(a.check_level())
        
        
        