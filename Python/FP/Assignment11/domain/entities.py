


class Student(object):
    
    def __init__(self, stud_id, stud_name):
        self.__stud_id = stud_id
        self.__stud_name = stud_name
    
    def get_stud_id(self):
        return self.__stud_id
    
    def get_stud_name(self):
        return self.__stud_name
    
    def set_stud_name(self, name):
        self.__stud_name = name
    
    def __eq__(self, other):
        return self.__stud_id == other.__stud_id
    
    def __str__(self):
        return "Student id: " + str(self.__stud_id) + "\n" + " Student name: " + self.__stud_name
    
    @staticmethod
    def read_student(line):
        parts = line.split(",")
        return Student(int(parts[0].strip()), parts[1].strip())
    
    @staticmethod
    def write_student(student):
        return str(student.__stud_id) + "," + student.__stud_name
    
    
class StudentDTO(object):
    
    def __init__(self, stud_name, average):
        self.__stud_name = stud_name
        self.__average = average
    
    def get_average(self):
        return self.__average
    
    def __str__(self):
        return self.__stud_name + " with an average of " + str(self.__average)


class DisciplineDTO(object):
    
    def __init__(self, dis_name, average):
        self.__dis_name = dis_name
        self.__average = average
    
    def get_average(self):
        return self.__average
    
    def __str__(self):
        return self.__dis_name + " with an average of " + str(self.__average)

    
class Discipline(object):
    
    def __init__(self, dis_id, dis_name):
        self.__dis_id = dis_id
        self.__dis_name = dis_name
    
    def get_dis_id(self):
        return self.__dis_id
    
    def get_dis_name(self):
        return self.__dis_name
    
    def set_dis_name(self, name):
        self.__dis_name = name
    
    def __eq__(self, other):
        return self.__dis_id == other.__dis_id
    
    def __str__(self):
        return "Discipline id: " + str(self.__dis_id) + "\n" + " Discipline name: " + self.__dis_name
    
    @staticmethod
    def read_discipline(line):
        parts = line.split(",")
        return Discipline(int(parts[0].strip()), parts[1].strip())

    
    @staticmethod
    def write_discipline(discipline):
        return str(discipline.__dis_id) + "," + discipline.__dis_name
    
    
class Grade(object):
    
    def __init__(self, student, discipline, value):
        self.__student = student
        self.__discipline = discipline
        self.__value = value

    def get_student(self):
        return self.__student

    def get_discipline(self):
        return self.__discipline

    def get_value(self):
        return self.__value    

    def set_value(self,value):
        self.__value = value

    def __eq__(self,other):
        return self.__student == other.__student and self.__discipline == other.__discipline and self.__value == other.__value

    def __str__(self):
        return self.__student.get_stud_name() + " got a " + str(self.__value) + " at " + self.__discipline.get_dis_name()
        
    @staticmethod
    def read_grade(line):
        parts = line.split(",")
        return Grade(Student(int(parts[0].strip()), ""), Discipline(int(parts[1].strip()), ""), float(parts[2].strip()))

    @staticmethod
    def write_grade(grade):
        return str(grade.__student.get_stud_id()) + "," + str(grade.__discipline.get_dis_id())+ "," + str(grade.__value)


class UndoRedoAction(object):
    
    def __init__(self, repo, action, rev_action, obj):
        self.__repo = repo
        self.__action = action
        self.__rev_action = rev_action
        self.__object = obj

    def get_repo(self):
        return self.__repo

    def get_action(self):
        return self.__action

    def get_rev_action(self):
        return self.__rev_action

    def get_object(self):
        return self.__object

    def execute(self):
        self.__action(self.__object)
    
    def get_opposite(self):
        return UndoRedoAction(self.get_repo(), self.get_rev_action(), self.get_action(), self.get_object())


class UndoRedoActionTwoObjects:
    def __init__(self, repo, action, obj1, obj2):
        self.__repo = repo
        self.__action = action
        self.__object1 = obj1
        self.__object2 = obj2

    def get_repo(self):
        return self.__repo

    def get_action(self):
        return self.__action

    def get_object1(self):
        return self.__object1
    
    def get_object2(self):
        return self.__object2

    def execute(self):
        self.__action(self.__object1, self.__object2)
    
    def get_opposite(self):
        return UndoRedoActionTwoObjects(self.get_repo(), self.get_action(), self.get_object2(), self.get_object1())
    


class ComplexUndoRedoAction(UndoRedoAction):
    
    def __init__(self):
        self.__undoRedoActions = []
    
    def add_action(self,action):
        self.__undoRedoActions.append(action)
    
    def get_action(self):
        return self.__undoRedoActions
    
    def execute(self):
        for i in range(len(self.__undoRedoActions)-1,-1,-1):
            self.__undoRedoActions[i].execute()

    def get_opposite(self):
        opposite = ComplexUndoRedoAction()
        for i in range(len(self.__undoRedoActions)-1,-1,-1):
            action = self.__undoRedoActions[i]
            opposite.add_action(action.get_opposite())
        return opposite   
    
    
    



