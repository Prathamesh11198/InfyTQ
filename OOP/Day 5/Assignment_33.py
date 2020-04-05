#OOPR-Tryout
#Start writing your code here
                                                
class OverdrawException(Exception):
    pass

class LimitReachedException(Exception):
    pass


class Account:
    def __init__(self, account_type, balance, min_balance):
        self.__account_type = account_type
        self.__balance = balance
        self.__min_balance = min_balance
        
    def get_min_balance(self):
        return self.__min_balance
        
    def get_account_type(self):
        return self.__account_type
        
    def get_balance(self):
        return self.__balance
        
    def set_balance(self, balance):
        self.__balance = balance

class Customer:
    def __init__(self, customer_id, customer_name, age, account):
        self.__customer_name = customer_name
        self.__customer_id = customer_id
        self.__account = account
        self.__age = age
        
    def get_customer_name(self):
        return self.__customer_name
        
    def get_customer_id(self):
        return self.__customer_id
    
    def get_age(self):
        return self.__age
        
    def get_account(self):
        return self.__account
        
    def withdraw(self, amount):
        if amount < self.__account.get_balance():
            if amount > self.__account.get_min_balance():
                self.account.set_balance(self.__account.get_balance()-amount)
            else:
                raise LimitReachedException("Err - Limit reached")
        else:
            raise OverdrawException("Err - Amount greater than balance")
        
    def take_card(self):
        print("Take card out from the ATM")
        
class PrivilegedCustomer(Customer):
    def __init__ (self, customer_id, customer_name,age,account, bonus_points):
        super().__init__(customer_id, customer_name, age, account)
        self.__bonus_points = bonus_points
        
    def get_bonus_points(self):
        return self.__bonus_points
        
    def __increase_bonus(self):
        if Customer.__account.get_balance() > 1000:
            self.__bonus_points += 1000
        else:
            self.__bonus_points += 2
            
    def withdraw(self, amount):
        super().withdraw(amount)
        self.__increase_bonus()
    
acc = Account("Saving", 1000, 500)
cust1 = PrivilegedCustomer(100, "Gopal", 43, acc,  100)

try:
    cust1.withdraw(500)
    
except OverdrawException as e:
    print(str(e))
    
except LimitReachedException as e:
    print(str(e))
    
    
    
        