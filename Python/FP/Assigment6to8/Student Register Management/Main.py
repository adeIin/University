# Main Module for Student Register Management

from Validations import ValidateStudent, ValidateDiscipline, ValidateGrade
from Model import StudentModel, DisciplineModel, GradeModel
from Repository import StudentRepository, DisciplineRepository, GradeRepository
from Service import StudentService, DisciplineService, GradeService
from UserInterface import UI

def Main():
    
    studModel = StudentModel()
    studValidate = ValidateStudent()
    studRepo = StudentRepository(studModel)
    studService = StudentService(studRepo, studModel, studValidate)

    disModel = DisciplineModel()
    disValidate = ValidateDiscipline()
    disRepo = DisciplineRepository(disModel)
    disService = DisciplineService(disRepo, disModel, disValidate)

    gradRepo = GradeRepository()
    gradModel = GradeModel()
    gradValidate = ValidateGrade()
    gradService = GradeService(gradRepo, disRepo, studRepo, gradModel, gradValidate)
    
    ui = UI(studService, disService, gradService)

    ui.run()

if __name__ == '__main__':
    Main()