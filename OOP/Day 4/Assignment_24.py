#OOPR-Assgn-24
#Start writing your code here

class Apparel:
    counter=100
    def __init__(self, price, item_type):
        self.__item_id=item_type[0].upper()+str(Apparel.counter+1)
        self.__price=price
        self.__item_type=item_type.title()
        Apparel.counter+=1
        
    def get_item_id(self):
        return self.__item_id
        
    def get_item_type(self):
        return self.__item_type
        
    def get_price(self):
        return self.__price
        
    def calculate_price(self):
        self.__price *=  1.05
        
    def set_price(self, price):
        self.__price=price
        
class Cotton(Apparel):
    def __init__(self, price,discount):
        super().__init__(price, "Cotton")
        self.__discount = discount
        
    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        price *= (1-((self.__discount)/100))
        price *= (1.05)
        self.set_price(price)
        
    def get_discount(self):
        return self.__discount
        
        
class Silk(Apparel):
    def __init__(self, price):
        super().__init__(price, "Silk")
        self.__points=0
        
    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        if price >10000:
            self.__points +=10
        else:
            self.__points += 3
        price = price * 1.10
        self.set_price(price)
        
    def get_points(self):
        return self.__points
        
a1 = Silk(500)
a1.calculate_price()