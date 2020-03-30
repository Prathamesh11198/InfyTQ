#OOPR-Assgn-13
#Start writing your code here

class Classroom:
    classroom_list = ["A", "B", "C", "D"]
    
    @staticmethod
    def search_classroom(class_room):
        lst = []
        for room in Classroom.classroom_list:
            lst.append(room.lower())
            
        if class_room.lower() in lst:
            return "Found"
        else:
            return -1
            
print(Classroom.search_classroom("C"))