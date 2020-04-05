#OOPR-Exer-8
class Juggler:
    def __init__(self,name):
        self.__name=name

    def juggles(self, jugglingitem):
        #write the code to make the juggler juggle
        print(self.__name," is juggling with ",jugglingitem.get_name())

class JugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
        
        
Jack = Juggler("Jack Bremlov")
jack_item = JugglingItem("knives")
Jack.juggles(jack_item)
Antony = Juggler("Anthony Gatto")
antony_item = JugglingItem("balls")
Antony.juggles(antony_item)