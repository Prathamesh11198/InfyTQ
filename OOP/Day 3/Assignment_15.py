#OOPR-Assgn-15
#Start writing your code here

class Parrot:
    __counter = 7000
    def __init__(self, name, color):
        self.__name = name
        self.__color = color
        self.__unique_number = Parrot.__counter+1
        Parrot.__counter += 1
        
    def get_name(self):
        return self.__name
    
    def get_unique_number(self):
        return self.__unique_number
    
    def get_color(self):
        return self.__color
        
p1 = Parrot("A", "Blue")
p2 = Parrot("B", "Red")
p3 = Parrot("C", "Red")
p4 = Parrot("D", "Red")
p5 = Parrot("E", "Red")
p6 = Parrot("F", "Red")
print(Parrot._Parrot__counter)