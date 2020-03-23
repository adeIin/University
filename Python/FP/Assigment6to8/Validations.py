# Validations Module for Student Register Management
#from Domain import Student, Discipline, Grade
from Exceptionsss import StudentException, DisciplineException, GradeException
    
class ValidateStudent:
    def validateId(self, student):
        '''
            Function that validates a student ID
            input: student - a student
            output: - if the student is valid
            raises: StudentException("Invalid student ID!\n") if the ID of the student is not valid
        '''
        if student.studentID < 0:
            raise StudentException("Invalid student ID!\n")

class ValidateDiscipline:
    def validateId(self, discipline):
        '''
            Function that validates a discipline ID
            input: discipline - a discipline
            output: - if the discipline ID is valid
            raises: DisciplineException("Invalid discipline ID!\n") if the ID of the discipline is not valid
         '''
        if discipline.disciplineID < 0:
            raise DisciplineException("Invalid discipline ID!\n")

class ValidateGrade:
    def validateGradeValue(self, grade):
        '''
            Function that validates a grade value
            input: grade - a grade
            output: - if the grade value is valid
            raises: GradeException("Invalid grade value!\n") if the grade value is not valid
        '''
        if grade.gradeValue < 1 and grade.gradeValue > 10:
            raise GradeException("Invalid grade value!\n")
