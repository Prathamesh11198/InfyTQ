#OOPR-Assgn-3
#Start writing your code here

class Customer:
    def __init__(self):
        self.customer_name = None
        self.bill_amount = None
        
    def purchases(self):
        self.bill_amount = self.bill_amount * 0.95
        
    def pays_bill(self, amount):
        print(self.customer_name, " pays bill amount of bill ", amount)
        
cust1 = Customer()
cust1.customer_name = "ABC"
cust1.bill_amount = 5000
cust1.purchases()
cust1.pays_bill(cust1.bill_amount)