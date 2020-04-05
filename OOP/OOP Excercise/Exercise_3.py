#OOPR-Exer-3
#Start writing your code here
                                                    

class Employee:
    def __init__(self):
        self.name = None
        self.age = None
        self.salary = None
        
jack = Employee()
jack.name = "Jack"
jack.salary = 50000
jack.age = 28
jill = Employee()
jill.name = "jill"
jill.salary = 30000
jill.age = 25

print(jack.name," ",jack.salary," ",jack.age )
print(jill.name," ",jill.salary," ",jill.age)