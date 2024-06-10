class Room:
    def __init__(self, id, floor, seats) -> None:
        self.id= id
        self.floor= floor
        self.seats= seats
        self.area= self.seats*2
    def get_id(self):
        return self.id
    def get_floor(self):
        return self.floor
    def get_seats(self):
        return self.seats
    def get_area(self):
        return self.area

class Building:
    def __init__(self, name, address, floors) -> None:
        self.name=name
        self.address=address
        self.floors= floors
        self.rooms=[]

    def get_floors(self):
        return self.floors
    def get_rooms(self):
        return self.rooms
    def add_room(self, room: Room):
        if room.floor >= min(self.floors) and  room.floor <= max(self.floors):
            if room not in self.rooms:
                self.rooms.append(room)
    def area(self):
        area_tot=0
        for i in self.rooms:
            area_tot+= i.get_area()
        return area_tot
    



class Person:
    def __init__(self, cf, name, surname, age) -> None:
        self.cf=cf
        self.name= name
        self.surname=surname
        self.age=age
class Student(Person):
    def __init__(self, cf, name, surname, age, group= None) -> None:
        super().__init__(cf, name, surname, age)   
        self.group= group
    def set_group(self, group):
        self.group= group

class Lecturer(Person):
    def __init__(self, cf, name, surname, age) -> None:
        super().__init__(cf, name, surname, age)

class Group:
    def __init__(self, name, limit) -> None:
        self.name=name
        self.limit= limit
        self.students= []
        self.lecturers=[]

    def get_name(self):
        return self.name
    def get_limit(self):
        return self.limit
    def get_students(self):
        return self.students
    #def get_limit_lecturers(self):
     #   limit_lecturers=1
    

    def add_student(self,student):
        for i in self.students:
            if i.get_limit > len(self.students):
                self.students.append(student)
        return self.students  
    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)
        return self.lecturers        

    
        
        

class Course:
    def __init__(self, name):
        self.name = name
        self.groups = []

    def register(self, student: Student):
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                group.add_student(student)
                student.set_group(group)
        
        

    def get_groups(self):
        return self.groups

    def add_group(self, group: Group):
        self.groups.append(group)
