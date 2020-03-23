# Service Module for Student Register Management

#from Repository import StudentRepository, DisciplineRepository, GradeRepository
#from Model import StudentModel, DisciplineModel, GradeModel
#from Validations import ValidateStudent, ValidateDiscipline, ValidateGrade
  
class StudentService:
    def __init__(self, studRepo, studModel, studValidate):
        self.repository = studRepo
        self.model = studModel
        self.validate = studValidate

    def addStudent(self, studentID, studentName):
        '''
            Function that creates a student based on an ID and on a name
            validates the student
            adds the student to the student register
            input: studentID - integer
                   studentName - string
            output: -
        '''
        student = self.model.createStudent(studentID, studentName)
        self.validate.validateId(student)
        self.repository.addStudent(student)
    
    def removeStudent(self, studID):
        '''
            Function that removes a student from the register based on its ID
            input: studID - integer
            output: - 
        '''
        self.repository.removeStudent(studID)
    
    def updateStudentId(self, studID, newID):
        '''
            Function that updates a student ID by creating a test stundent in order tio validate the ID and then updating the student
            input:  oldID - integer
                    newID - integer
            output: -
        '''
        testStudent = self.model.createStudent(newID, "name")
        self.validate.validateId(testStudent)
        self.repository.updateStudentID(studID, newID)
    
    def updateStudentName(self, studID, newName):
        '''
            Function that updates a student name
            input: studID - integer
                   newName - string
            output: -
        '''
        self.repository.updateStudentName(studID, newName)

class DisciplineService:
    def __init__(self, disRepo, disModel, disValidate):
        self.repository = disRepo
        self.model = disModel
        self.validate = disValidate
    
    def addDiscipline(self, disciplineID, disciplineName):
        '''
            Function that creates a discipline based on an ID and on a name
            validates the discipline
            adds the discipline to the discipline register
            input: disciplineID - integer
                   disciplineName - string
            output: -
        '''
        discipline = self.model.createDiscipline(disciplineID, disciplineName)
        self.validate.validateId(discipline)
        self.repository.addDiscipline(discipline)

    def removeDiscipline(self, disID):
        '''
            Function that removes a discipline from the register
            input: disID - integer
            output: -
        '''
        self.repository.removeDiscipline(disID)
    
    def updateDisciplineId(self, disID, newID):
        '''
            Function that updates a discipline ID by creating a test discipline in order to validate the ID and then updating the discipline
            input:  oldID - integer
                    newID - integer
            output: -
        '''
        testDiscipline = self.model.createDiscipline(newID, "name")
        self.validate.validateId(testDiscipline)
        self.repository.updateDisciplineID(disID, newID)
    
    def updateDisciplineName(self, disID, newName):
        '''
            Function that updates a discipline's name
            input: disID - integer
                   newName - string
            output: - 
        '''
        self.repository.updateDisciplineName(disID, newName)

class GradeService:
    def __init__(self, gradRepo, disRepo, studRepo, gradModel, gradValidate):
        self.gradeRepository = gradRepo
        self.disciplineRepository = disRepo
        self.studentRepository = studRepo
        self.model = gradModel
        self.validate = gradValidate
    
    def initialiseGradeRegister(self, n):
        '''
            Function that initialise the grade register by adding n random grades
            input: n - integer
            output: -
        '''
        disIdList = self.disciplineRepository.exportDisciplinesId()
        studIdList = self.studentRepository.exportStudentsId()
        self.gradeRepository.initialiseGradeRegister(n, disIdList, studIdList)
    
    def addGrade(self, disID, studID, gradValue):
        '''
            Function that creates a grade based on a discipline ID, a student ID and a grade value
            validates the grade
            checks if the discipline ID and the student ID exists in the registers
            adds the grade to the grade register
            input: disciplineID - integer
                   disciplineName - string
            output: -
        '''
        grade = self.model.createGrade(disID, studID, gradValue)
        self.validate.validateGradeValue(grade)
        self.disciplineRepository.checkIfDisciplineExists(disID)
        self.studentRepository.checkIfStudentExists(studID)
        self.gradeRepository.addGrade(grade)
    
    def removeStudentGrades(self, studID):
        '''
            Function that removes all the grades of a student
            input: studId - integer
            output: -
            raises: -
        '''
        self.gradeRepository.removeGradesOfaStudent(studID)
    
    def removeDisciplineGrades(self, disID):
        '''
            Function that removes all the grades at a discipline
            input: disID - integer
            output: -
            raises: -
        '''
        self.gradeRepository.removeGradesFromDiscipline(disID)

