from domain.validators import ValidateStudent, ValidateDiscipline, ValidateGrade
from domain.entities import Student, Discipline, Grade
from infrastructure.repository import RepositoryUniqueElements, RepositoryMultipleElements, \
    FileRepositoryUniqueElements, FileRepositoryMultipleElements, UndoRedoStack, \
    BinaryFileRepositoryUniqueElements, BinaryFileRepositoryMultipleElements
from business.services import StudentService, DisciplineService, GradeService, UndoRedoService
from presentation.userinterface import Console


def program_configuration():
    validStud = ValidateStudent()
    validDis = ValidateDiscipline()
    validGrad = ValidateGrade()

    f = open("settings.txt", "r")
    f1 = f.readlines()
    for x in f1:
        if "inmemory" in x:
            repository_flag = 1
        elif "textfile" in x:
            repository_flag = 2
        else:
            if "binaryfile" in x:
                repository_flag = 3

    if repository_flag == 1:
        repoStud = RepositoryUniqueElements()
        repoDis = RepositoryUniqueElements()
        repoGrad = RepositoryMultipleElements()
        undoStack = UndoRedoStack()
        redoStack = UndoRedoStack()
    elif repository_flag == 2:
        repoStud = FileRepositoryUniqueElements("students.txt", Student.read_student, Student.write_student)
        repoDis = FileRepositoryUniqueElements("disciplines.txt", Discipline.read_discipline,
                                               Discipline.write_discipline)
        repoGrad = FileRepositoryMultipleElements("grades.txt", Grade.read_grade, Grade.write_grade)
        undoStack = UndoRedoStack()
        redoStack = UndoRedoStack()
    else:
        repoStud = BinaryFileRepositoryUniqueElements("students.pickle", Student.read_student, Student.write_student)
        repoDis = BinaryFileRepositoryUniqueElements("disciplines.pickle", Discipline.read_discipline,
                                                     Discipline.write_discipline)
        repoGrad = BinaryFileRepositoryMultipleElements("grades.pickle", Grade.read_grade, Grade.write_grade)
        undoStack = UndoRedoStack()
        redoStack = UndoRedoStack()

    fileSrvStud = StudentService(repoStud, validStud, undoStack, redoStack)
    fileSrvDis = DisciplineService(repoDis, validDis, undoStack, redoStack)
    fileSrvGrad = GradeService(repoStud, repoDis, repoGrad, validGrad, undoStack, redoStack)

    srvUndoRedo = UndoRedoService(undoStack, redoStack)

    ui = Console(fileSrvStud, fileSrvDis, fileSrvGrad, srvUndoRedo)

    ui.run()


program_configuration()
