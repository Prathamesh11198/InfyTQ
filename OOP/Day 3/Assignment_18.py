#OOPR-Assgn-18
#Start writing your code here

items=[]

class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id = item_id.upper()
        self.__description = description.upper()
        self.__price_per_quantity = price_per_quantity
        items.append(self)
        
    def get_item_id(self):
        return self.__item_id
        
    def get_description(self):
        return self.__description
        
    def get_price_per_quantity(self):
        return self.__price_per_quantity
        
        
class Bill:
    counter=1000
    def __init__(self):
        self.__bill_id = 1000
        self.__bill_amount = 0
        
    def generate_bill_amount(self,item_quantity, items):
        self.__bill_amount = 0
        for key,value in item_quantity.items():
            for item in items:
                if item.get_item_id() == key.upper():
                    self.__bill_amount += value*item.get_price_per_quantity()
                    continue
        if self.__bill_amount > 0:
            self.__bill_id = "B" + str(Bill.counter+1)
            Bill.counter += 1
            
    def get_bill_id(self):
        return self.__bill_id
        
    def get_bill_amount(self):
        return self.__bill_amount
        
        
class Customer:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__payment_status = None
        
    def pays_bill(self, bill):
        self.__payment_status = "Paid"
        print(self.get_customer_name())
        print(bill.get_bill_id())
        print(bill.get_bill_amount())
        
    def get_customer_name(self):
        return self.__customer_name
        
    def get_payment_status(self):
        return self.__payment_status
        
item_quantity = {'I1':6, 'I2':2, 'I3':4}

c=Customer("ABC")

i1=Item("I1", "A", 100)
i2=Item("I2", "B", 50)
i3=Item("I3", "C", 20)

b=Bill()
b.generate_bill_amount(item_quantity, items)
b.generate_bill_amount(item_quantity, items)
b.generate_bill_amount(item_quantity, items)
b.generate_bill_amount(item_quantity, items)
b.generate_bill_amount(item_quantity, items)

c.pays_bill(b)