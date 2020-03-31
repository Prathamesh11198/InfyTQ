#OOPR-Assgn-19
#Start writing your code here

source = ["delhi"]
dest = ["mumbai", "chennai", "pune", "kolkata"]

class Ticket:
    counter = 0
    
    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__ticket_id = None
        self.__destination = destination
        self.__source = source
        
    def get_passenger_name(self):
        return self.__passenger_name
    
    def get_ticket_id(self):
        return self.__ticket_id
        
    def get_destination(self):
        return self.__destination
        
    def get_source(self):
        return self.__source
        
    def validate_source_destination(self):
        if self.__source.lower() in source and self.__destination.lower() in dest:
            return True
        else:
            return False
        
    def generate_ticket(self):
        if self.validate_source_destination():
            tk = self.__source[0].upper()+self.__destination[0].upper()
            if Ticket.counter < 9:
                self.__ticket_id = tk + "0" + str(Ticket.counter+1)
            else:
                self.__ticket_id = tk + str(Ticket.counter+1)
        else:
            self.__ticket_id = None
            
        Ticket.counter += 1
    
t1 = Ticket("ABC", "delhi", "pune")
t1.generate_ticket()
t2 = Ticket("ABC", "delhi", "pune")
t2.generate_ticket()

print(t1.get_ticket_id())
print(t2.get_ticket_id())


