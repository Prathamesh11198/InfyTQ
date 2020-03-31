#OOPR-Assgn-22
class Multiplex:
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=["M1-11",None]
    __list_ticket_price=[150,200]
    
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
        
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
        
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
            
    def get_total_price(self):
        return self.__total_price
        
    def get_seat_numbers(self):
        return self.__seat_numbers
        
    def book_ticket(self, movie_name, number_of_tickets):
        if movie_name in self.__list_movie_name:
            movie_ind = self.__list_movie_name.index(movie_name)
            if self.__list_total_tickets[movie_ind] >= number_of_tickets:
                self.__seat_numbers = self.generate_seat_number(movie_ind, number_of_tickets)
                self.__total_price = number_of_tickets*self.__list_ticket_price[movie_ind]
            else:
                return -1
        else:
            return 0
        
    def  generate_seat_number(self,movie_index, number_of_tickets):
        self.__list_total_tickets[movie_index] = self.__list_total_tickets[movie_index] - number_of_tickets
        lst = []
        
        last_ticket = self.__list_last_seat_number[movie_index]
        if last_ticket == None:
            last_no = 1
        else:
            last_no = last_ticket.split("-")
            last_no = int(last_no[1])+1
            
        for i in range(last_no, number_of_tickets+last_no):
            ticket_no = "M"+str(movie_index+1)+"-"+str(i)
            lst.append(ticket_no)
            self.__list_last_seat_number[movie_index] = lst[-1]
            
        return lst
        
booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")


booking2=Multiplex()
status=booking2.book_ticket("movie2",6)

if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())