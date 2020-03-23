# Model Module For Student Register Management

from Domain import Student, Discipline, Grade

class StudentModel:
    def createStudent(self, studentID, studentName):
        '''
            Function that creates a student based on an ID and on a name
            input: studentID - integer
                   studentName - string
            output: student - a student
        '''
        student = Student(studentID, studentName)
        return student
    
    def updateStudentId(self, student, newID):
        '''
            Function that updates a student id
            input: student - a student
                   newID - integer
            output: -
        '''
        student.studentID = newID
    
    def updateStudentName(self, student, newName):
        '''
            Function that updates a student name
            input: student - a student
                   newName - string
            output: -
        '''
        student.studentName = newName

class DisciplineModel:
    def createDiscipline(self, disciplineID, disciplineName):
        '''
            Function that creates a discipline based on an ID and on a name

            input: disciplineID - integer
                   disciplieName - string
            output: discipline - a discipline
        '''
        discipline = Discipline(disciplineID, disciplineName)
        return discipline
    
    def updateDisciplineID(self, discipline, newID):
        '''
            Function that updates a discipline id
            input: discipline - a discipline
                   newID - integer
            output: -
        '''
        discipline.disciplineID = newID
    
    def updateDisciplineName(self, discipline, newName):
        '''
            Function that updates a discipline name
            input: discipline - a discipline
                   newName - string
            output: -
        '''
        discipline.disciplineName = newName
  
class GradeModel:
    def createGrade(self, disciplineID, studentID, gradeValue):
        '''
            Function that creates a grade based on a discipline ID, a student ID and a grade value
            input: disciplineID - integer
                   studentID - integer
                   gradeValue - integer
            output: grade - a grade
        '''
        grade = Grade(disciplineID, studentID, gradeValue)
        return grade
