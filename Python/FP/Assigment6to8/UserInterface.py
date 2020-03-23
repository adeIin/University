# User Interface for Student Register Management

#from Service import StudentService, DisciplineService
from Exceptionsss import StudentException, DisciplineException, GradeException
  
class UI:
    def __init__(self, studService, disService, gradService):
        self.studentService = studService
        self.disciplineService = disService
        self.gradeService = gradService
    
    def printMenuCommands(self):
        print("Student Register Management application commands: ")
        print("           (1) to add a student.")
        print("           (2) to add a discipline.")
        print("           (3) to add a grade.")
        print("           (4) to list students.")
        print("           (5) to list disciplines.")
        print("           (6) to list grades.")
        print("           (7) to remove a student.")
        print("           (8) to remove a discipline.")
        print("           (9) to update student ID.")
        print("           (10) to update student name.")
        print("           (11) to upadate discipline ID.")
        print("           (12) to update discipline name.")
        print("           (13) to ")
        print("           (14) to ")
        print("           (0) to exit.")
        print("")

    def readNumerical(self, msg, typ):
        x = input(msg)
        while True:
            try:
                x = typ(x)
                return x
            except ValueError:
                print("Invalid numerical value!\n")
                x = input(msg)
    
    def addStudent(self):
        studID = self.readNumerical("Insert student ID: ", int)
        studName = input("Insert student name: ")
        print("")
        try:
            self.studentService.addStudent(studID, studName)
            print("Student successfully added!\n")
        except StudentException as studEx:
            print(str(studEx))
    
    def addDiscipline(self):
        disID = self.readNumerical("Insert discipline ID: ", int)
        disName = input("Insert discipline name: ")
        print("")
        try:
            self.disciplineService.addDiscipline(disID, disName)
            print("Discipline successfully added!\n")           
        except DisciplineException as disEx:
            print(str(disEx))

    def addGrade(self):
        disID = self.readNumerical("Insert discipline ID: ", int)
        studID = self.readNumerical("Insert student ID: ", int)
        gradeValue = self.readNumerical("Insert grade value: ", int)
        print("")
        try:
            self.gradeService.addGrade(disID, studID, gradeValue)
            print("Grade successfully added!\n")
        except (GradeException, DisciplineException, StudentException) as ex:
            print(str(ex))
    
    def removeStudent(self):
        studID = self.readNumerical("Insert student ID: ", int)
        print("")
        try:
            self.studentService.removeStudent(studID)
            print("Student successfully removed!")
            self.gradeService.removeStudentGrades(studID)
            print("Student grades successfully removed!\n")
        except StudentException as studEx:
            print(str(studEx))

    def removeDiscipline(self):
        disID = self.readNumerical("Insert discipline ID: ", int)
        print("")
        try:
            self.disciplineService.removeDiscipline(disID)
            print("Discipline successfully removed!")
            self.gradeService.removeDisciplineGrades(disID)
            print("Grades of all students at this discipline successfully removed!\n")
        except DisciplineException as disEx:
            print(str(disEx))

    def listStudents(self):
        studentRegister = self.studentService.repository.studentRegister
        if studentRegister == []:
            print("Student Register empty!\n")
            return
        i = 1
        for x in studentRegister:
            print("Student number", str(i), "in register:")
            print("     ID:", x.studentID)
            print("     Name:", x.studentName)
            print("")
            i += 1
    
    def listDisciplines(self):
        disciplineRegister = self.disciplineService.repository.disciplineRegister
        if disciplineRegister == []:
            print("Discipline Register empty!\n")
            return
        i = 1
        for x in disciplineRegister:
            print("Discipline number", str(i), "in register:")
            print("     ID:", x.disciplineID)
            print("     Name:", x.disciplineName)
            print("")
            i += 1
    
    def listGrades(self):
        gradeRegister = self.gradeService.gradeRepository.gradeRegister
        if gradeRegister == []:
            print("Grade Register empty!\n")
            return
        for x in gradeRegister:
            print("Discipline", x.disciplineID, "student", x.studentID, "grade value", x.gradeValue, "\n")
    
    def updateStudentId(self):
        studID = self.readNumerical("Insert student ID: ", int)
        newID = self.readNumerical("Insert new student ID: ", int)
        print("")
        try:
            self.studentService.updateStudentId(studID, newID)
            print("Student ID successfully updated!\n")
        except StudentException as studEx:
            print(str(studEx))

    def updateStudentName(self):
        studID = self.readNumerical("Insert student ID: ", int)
        newName = input("Insert student's new name: ")
        print("")
        try:
            self.studentService.updateStudentName(studID, newName)
            print("Student's name successfully updated!")
        except StudentException as studEx:
            print(str(studEx))
    
    def updateDisciplineId(self):
        disID = self.readNumerical("Insert discipline ID: ", int)
        newID = self.readNumerical("Insert new discipline ID: ", int)
        print("")
        try:
            self.disciplineService.updateDisciplineId(disID, newID)
            print("Discipline ID successfully updated!\n")
        except DisciplineException as disEx:
            print(str(disEx))

    def updateDisciplineName(self):
        disID = self.readNumerical("Insert discipline ID: ", int)
        newName = input("Insert discipline's new name: ")
        print("")
        try:
            self.disciplineService.updateDisciplineName(disID, newName)
            print("Discipline's name successfully updated!\n")
        except DisciplineException as disEx:
            print(str(disEx))

    def run(self):

        self.studentService.repository.initialiseStudentRegister(5)
        self.disciplineService.repository.initialiseDisciplineRegister(5)
        self.gradeService.initialiseGradeRegister(10)

        commands = {
            '1': self.addStudent,
            '2': self.addDiscipline,
            '3': self.addGrade,
            '4': self.listStudents,
            '5': self.listDisciplines,
            '6': self.listGrades,
            '7': self.removeStudent,
            '8': self.removeDiscipline,
            '9': self.updateStudentId,
            '10': self.updateStudentName,
            '11': self.updateDisciplineId,
            '12': self.updateDisciplineName
        }

        while True:
            self.printMenuCommands()
            cmd = input("Insert command: ")
            print ("")
            if cmd == '0':
                return
            if cmd not in commands:
                print("Invalid command!\n")
            else:
                commands[cmd]()
