# Repository Module for Students Register Management

from Domain import Student, Discipline, Grade
from Exceptionsss import StudentException, DisciplineException, GradeException
import random
  
class StudentRepository:
    def __init__(self, studModel):
        self.studentRegister = []
        self.model = studModel
    
    def addTwoNumbers(self, a, b):
        return a + b
    
    def initialiseStudentRegister(self, n):
        '''
            Function that initialise the student register by adding n random students
            input: n - integer
            output: -
            raises: -
        '''
        listOfNames = [
            "Abel Crosby", 
            "Jaylan Church", 
            "Kolten Beard", 
            "Alfonso Cole", 
            "Liana Travis", 
            "Jaidyn Benton", 
            "Jazlene Grimes", 
            "Kane Obrien", 
            "Cory Tyler", 
            "Joyce Hopkins", 
            "Adelyn Richardson", 
            "Savannah Kent", 
            "Jase Frazier", 
            "Kaeden Mills", 
            "Liam Wu", 
            "Zaiden Knight", 
            "Efrain Olsen", 
            "Zackery Olsen", 
            "Luciano Dorsey", 
            "Waylon White", 
            "Raul Joseph", 
            "Magdalena Fitzgerald", 
            "Reese Mccann", 
            "Jaylee Spencer", 
            "Litzy Olsen", 
            "Emery Summers", 
            "Deangelo Jimenez", 
            "Trace Macias", 
            "Hana Padilla", 
            "Nash Best", 
            "Jakayla Shannon", 
            "Kamden Green", 
            "Crystal Cain", 
            "Niko Liu", 
            "Aniyah Foley", 
            "Colin Castro", 
            "Stephany Davies", 
            "Jacquelyn Oneill", 
            "Alma Riddle", 
            "Ryland White", 
            "Mariyah Conley", 
            "Karlee Lang", 
            "Jaeden Espinoza", 
            "Cruz Valenzuela", 
            "Priscilla Coleman", 
            "Amiah Nash", 
            "Matias Briggs", 
            "Paisley Porter", 
            "Dulce Hall", 
            "Parker Molina", 
            "Oscar Wolf", 
            "Richard Marshall", 
            "Kiley Friedman", 
            "Charity Spence", 
            "Jamir Steele", 
            "Nathanial Blanchard", 
            "Veronica Sutton", 
            "Misael Cooley", 
            "Claudia Wilkins", 
            "Madelyn Trujillo", 
            "Julius Parrish", 
            "Brandon Graham", 
            "Yaretzi Robbins", 
            "Emilee Holder", 
            "Elvis Thompson", 
            "Trevin Ferrell", 
            "Slade Norris", 
            "Carla Pruitt", 
            "Josh Love", 
            "Weston Steele", 
            "Phoebe Wilkerson", 
            "Memphis Dodson", 
            "Ibrahim White", 
            "Amiya Pierce", 
            "Kaiya Mcintosh", 
            "Tamara Reyes", 
            "Carley Lutz", 
            "Asia Andrade", 
            "Isabell Curry", 
            "Ayden Clements", 
            "Princess Hunter", 
            "Caroline Mitchell", 
            "Dakota Browning", 
            "Dangelo Hurley", 
            "Tyrone Chambers", 
            "Darien Walker"]
        for x in range(1, n + 1):
            studName = random.choice(listOfNames)
            listOfNames.remove(studName)
            studID = x * 14
            student = Student(studID, studName)
            self.studentRegister.append(student)
    
    def exportStudentsId(self):
        '''
            Function that exports the disciplines IDs as a list
            input: -
            output: disIdList - a list
        '''
        studIdList = []
        for x in self.studentRegister:
            studIdList.append(x.studentID)
        return studIdList
    
    def addStudent(self, student):
        '''
            Function that adds a student to the studentRegister
            input: student - a student
            output: - if the student was added successfully
            raises: StudentException("Student ID already exists!\n) if the student ID is already in the register
        '''
        for x in self.studentRegister:
            if x.studentID == student.studentID:
                raise StudentException("Student ID already exists!\n")
        self.studentRegister.append(student)
    
    def checkIfStudentExists(self, studID):
        '''
            Function that checks if an ID exists in the student register
            input: studID - integer
            output: - if the ID exists
            raises: StudentException("Student ID does not exist!\n") if the ID does not exist
        '''
        for x in self.studentRegister:
            if x.studentID == studID:
                return
        raise StudentException("Student ID does not exist!\n")

    def removeStudent(self, studID):
        '''
            Function that removes a student from the student register
            input: studID - integer
            output: -
            raises: StudentException("Student ID not found!\n") if the ID does not exist in the register
        '''
        for x in self.studentRegister:
            if x.studentID == studID:
                self.studentRegister.remove(x)
                return
        raise StudentException("Student ID not found!\n")

    def updateStudentID(self, studID, newID):
        '''
            Function that updates a student ID
            input: studID
            output: -
            raises: StudentException("Student ID not found!\n) if the student id is not in the register
        '''
        for x in self.studentRegister:
            if x.studentID == studID:
                self.model.updateStudentId(x, newID)
                return
        raise StudentException("Student ID not found!\n")

    def updateStudentName(self, studID, newName):
        '''
            Function that updates a student name
            input: studID - integer
                   newName - string
            output: -
            raises: StudentException("Student ID not found!\n") if the student ID is not in the register
        '''
        for x in self.studentRegister:
            if x.studentID == studID:
                self.model.updateStudentName(x, newName)
                return
        raise StudentException("Student ID not found!\n")

class DisciplineRepository:
    def __init__(self, disModel):
        self.disciplineRegister = []
        self.model = disModel
    
    def initialiseDisciplineRegister(self, n):
        '''
            Function that initialises the discipline register by adding n random disciplines
            input: n - integer
            output: -
            raises: -
        '''
        listOfDisciplines = [
            "Logic in computer science",
            "Algorithms",
            "Artificial intelligence",
            "Data structures",
            "Computer architecture",
            "Computer graphics",
            "Computer communications",
            "Computer security and reliability",
            "Cryptography",
            "Algebraic computation",
            "Computational biology",
            "Computational chemistry",
            "Computational mathematics",
            "Computational neuroscience",
            "Computational number theory",
            "Computational physics",
            "Computer-aided engineering",
            "Computational fluid dynamics",
            "Scientific computing",
            "History of computer hardware",
            "History of computer science",
            "Data management",
            "Data mining",
            "Information architecture",
            "Knowledge management",
            "Operating systems",
            "High-performance computing",
            "Programming languages",
            "Object-oriented programming",
            "Program semantics",
            "Type theory",
            "Quantum computing",
            "Software engineering",
            "Theory of computation",
            "Automata theory",
            "Computability theory",
            "Computational complexity theory",
            "Concurrency theory",
            "VLSI design"]
        for x in range(1, n + 1):
            disName = random.choice(listOfDisciplines)
            listOfDisciplines.remove(disName)
            disID = x * 12
            discipline = Discipline(disID, disName)
            self.disciplineRegister.append(discipline)
        
    def exportDisciplinesId(self):
        '''
            Function that exports the disciplines IDs as a list
            input: -
            output: disIdList - a list
        '''
        disIdList = []
        for x in self.disciplineRegister:
            disIdList.append(x.disciplineID)
        return disIdList

    def addDiscipline(self, discipline):
        '''
            Function that adds a discipline to the disciplineRegister
            input: discipline - a discipline
            output: - if the discipline was added successfully
            raises: DisciplineException("Discippline ID already exists!\n) if the discipline ID is already in the register
        '''
        for x in self.disciplineRegister:
            if x.disciplineID == discipline.disciplineID:
                raise DisciplineException("Discipline ID already exists!\n")
        self.disciplineRegister.append(discipline)
    
    def checkIfDisciplineExists(self, disID):
        '''
            Function that checks if an ID exists in the discipline register
            input: disID - integer
            output: - if the ID exists
            raises: DisciplineException("Discipline ID does not exist!\n") if the ID does not exist
        '''
        for x in self.disciplineRegister:
            if x.disciplineID == disID:
                return
        raise DisciplineException("Discipline ID does not exist!\n")

    def removeDiscipline(self, disID):
        '''
            Function that removes a discipline from the discipline register
            input: disID - integer
            output: -
            raises: DisciplineException("Discipline ID not found!\n") if the ID does not exist in the register
        '''
        for x in self.disciplineRegister:
            if x.disciplineID == disID:
                self.disciplineRegister.remove(x)
                return
        raise DisciplineException("Discipline ID not found!\n")

    def updateDisciplineID(self, disID, newID):
        '''
            Function that updates the ID of a discipline
            input: disID - integer
                   newID - integer
            output: -
            raises: DisciplineException("Discipline ID not found!\n") if the discipline ID is not in the register
        '''
        for x in self.disciplineRegister:
            if x.disciplineID == disID:
                self.model.updateDisciplineID(x, newID)
                return
        raise DisciplineException("Discipline ID not found!\n")

    def updateDisciplineName(self, disID, newName):
        '''
            Function that updates a discipline name
            input: disID - integer
                   newName - string
            output: -
            raises: DisciplineException("Discipline ID not found!\n") if the discipline ID is not in the register
        '''
        for x in self.disciplineRegister:
            if x.disciplineID == disID:
                self.model.updateDisciplineName(x, newName)
                return
        raise DisciplineException("Discipline ID not found!\n")
    
class GradeRepository:
    def __init__(self):
        self.gradeRegister = []
    
    def initialiseGradeRegister(self, n, disIdList, studIdList):
        '''
            Function that initialise grade register by adding n random grades at random disciplines and students
            input: n - integer
                   disIdList - list
                   studIdList - list
            output: -
        '''
        for x in range(0, n):
            x += 1
            disId = random.choice(disIdList)
            studId = random.choice(studIdList)
            gradVal = random.randint(1, 10)
            grade = Grade(disId, studId, gradVal)
            self.gradeRegister.append(grade)
    
    def addGrade(self, grade):
        '''
            Function that adds a grade to the grade register
            input: grade - a grade
            output: -
            raises: -
        '''
        self.gradeRegister.append(grade)
    
    def removeGrade(self, grade):
        '''
            Function that removes a grade from the grade register
            input: grade
            output: -
            raises: GradeException("Grade not found\n") if the grade does not exist
        '''
        for x in self.gradeRegister:
            if x == grade:
                self.gradeRegister.remove(x)
                return
        raise GradeException("Grade not found\n")
    
    def removeGradesOfaStudent(self, studID):
        '''
            Function that removes all grades of a student
            input: studID - integer
            output: -
        '''
        for x in range(len(self.gradeRegister) -1, -1, -1):
            if self.gradeRegister[x].studentID == studID:
                self.gradeRegister.remove(self.gradeRegister[x])
    
    def removeGradesFromDiscipline(self, disID):
        '''
            Function that removes all grades from a discipline
            input: disID - integer
            output: -
            raises: -
        '''
        for x in range(len(self.gradeRegister) -1, -1, -1):
            if self.gradeRegister[x].disciplineID == disID:
                self.gradeRegister.remove(self.gradeRegister[x])


