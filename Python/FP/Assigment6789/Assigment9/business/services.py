from domain.entities import Student, Discipline, Grade, UndoRedoAction, UndoRedoActionTwoObjects, ComplexUndoRedoAction, \
    StudentDTO, DisciplineDTO
import re
from sys import flags
from sre_constants import SRE_FLAG_IGNORECASE


class StudentService(object):

    def __init__(self, repoStud, validStud, undoStack, redoStack):
        self.__studentRepository = repoStud
        self.__studentValidator = validStud
        self.__undoStack = undoStack
        self.__redoStack = redoStack

    def add_student(self, stud_id, stud_name):
        student = Student(stud_id, stud_name)
        self.__studentValidator.validate_student(student)
        self.__studentRepository.add(student)
        action = UndoRedoAction(self.__studentRepository, self.__studentRepository.remove, self.__studentRepository.add,
                                student)
        self.__undoStack.push(action)
        self.__redoStack.clear()

    def update_student_id(self, old_stud_id, new_stud_id):
        old_student = self.__studentRepository.search(Student(old_stud_id, ""))
        new_student = Student(new_stud_id, old_student.get_stud_name())
        self.__studentValidator.validate_student(new_student)
        self.__studentRepository.update(old_student, new_student)
        action = UndoRedoActionTwoObjects(self.__studentRepository, self.__studentRepository.update, new_student,
                                          old_student)
        self.__undoStack.push(action)
        self.__redoStack.clear()

    def update_student_name(self, stud_id, new_stud_name):
        old_student = self.__studentRepository.search(Student(stud_id, ""))
        new_student = Student(stud_id, new_stud_name)
        self.__studentValidator.validate_student(new_student)
        self.__studentRepository.update(old_student, new_student)
        action = UndoRedoActionTwoObjects(self.__studentRepository, self.__studentRepository.update, new_student,
                                          old_student)
        self.__undoStack.push(action)
        self.__redoStack.clear()

    def search_student_name(self, stud_name):
        students = self.__studentRepository.get_all()
        matched_students = []
        for student in students:
            x = re.search(stud_name, student.get_stud_name(), flags=SRE_FLAG_IGNORECASE)
            if x:
                matched_students.append(student)
        return matched_students

    def search_student_id(self, stud_id):
        student = self.__studentRepository.search(Student(stud_id, ""))
        return student

    def get_students(self):
        return self.__studentRepository.get_all()


class DisciplineService(object):

    def __init__(self, repoDis, validDis, undoStack, redoStack):
        self.__disciplineRepository = repoDis
        self.__disciplineValidator = validDis
        self.__undoStack = undoStack
        self.__redoStack = redoStack

    def add_discipline(self, dis_id, dis_name):
        discipline = Discipline(dis_id, dis_name)
        self.__disciplineValidator.validate_discipline(discipline)
        self.__disciplineRepository.add(discipline)
        action = UndoRedoAction(self.__disciplineRepository, self.__disciplineRepository.remove,
                                self.__disciplineRepository.add, discipline)
        self.__undoStack.push(action)
        self.__redoStack.clear()

    def update_discipline_id(self, old_dis_id, new_dis_id):
        old_discipline = self.__disciplineRepository.search(Discipline(old_dis_id, ""))
        new_discipline = Discipline(new_dis_id, old_discipline.get_dis_name())
        self.__disciplineValidator.validate_discipline(new_discipline)
        self.__disciplineRepository.update(old_discipline, new_discipline)
        action = UndoRedoActionTwoObjects(self.__disciplineRepository, self.__disciplineRepository.update,
                                          new_discipline, old_discipline)
        self.__undoStack.push(action)
        self.__redoStack.clear()

    def update_discipline_name(self, dis_id, new_dis_name):
        old_discipline = self.__disciplineRepository.search(Discipline(dis_id, ""))
        new_discipline = Discipline(dis_id, new_dis_name)
        self.__disciplineValidator.validate_discipline(new_discipline)
        self.__disciplineRepository.update(old_discipline, new_discipline)
        action = UndoRedoActionTwoObjects(self.__disciplineRepository, self.__disciplineRepository.update,
                                          new_discipline, old_discipline)
        self.__undoStack.push(action)
        self.__redoStack.clear()

    def search_discipline_name(self, dis_name):
        disciplines = self.__disciplineRepository.get_all()
        matched_disciplines = []
        for discipline in disciplines:
            x = re.search(dis_name, discipline.get_dis_name(), flags=SRE_FLAG_IGNORECASE)
            if x:
                matched_disciplines.append(discipline)
        return matched_disciplines

    def search_discipline_id(self, dis_id):
        discipline = self.__disciplineRepository.search(Discipline(dis_id, ""))
        return discipline

    def get_disciplines(self):
        return self.__disciplineRepository.get_all()


class GradeService(object):

    def __init__(self, repoStud, repoDis, repoGrad, validGrad, undoStack, redoStack):
        self.__studentRepository = repoStud
        self.__disciplineRepository = repoDis
        self.__gradeRepository = repoGrad
        self.__gradeValidator = validGrad
        self.__undoStack = undoStack
        self.__redoStack = redoStack

    def add_grade(self, stud_id, dis_id, grad_value):
        student = self.__studentRepository.search(Student(stud_id, ""))
        discipline = self.__disciplineRepository.search(Discipline(dis_id, ""))
        grade = Grade(student, discipline, grad_value)
        self.__gradeValidator.validate_grade(grade)
        self.__gradeRepository.add(grade)
        action = UndoRedoAction(self.__gradeRepository, self.__gradeRepository.remove, self.__gradeRepository.add,
                                grade)
        self.__undoStack.push(action)
        self.__redoStack.clear()

    def remove_student_and_grades_by_id(self, stud_id):
        action = ComplexUndoRedoAction()
        student = self.__studentRepository.search(Student(stud_id, ""))
        grades = self.__gradeRepository.get_all()
        for grade in grades:
            if grade.get_student() == student:
                self.__gradeRepository.remove(grade)
                grade_action = UndoRedoAction(self.__gradeRepository, self.__gradeRepository.add,
                                              self.__gradeRepository.remove, grade)
                action.add_action(grade_action)
        self.__studentRepository.remove(student)
        student_action = UndoRedoAction(self.__studentRepository, self.__studentRepository.add,
                                        self.__studentRepository.remove, student)
        action.add_action(student_action)
        self.__undoStack.push(action)
        self.__redoStack.clear()

    def remove_discipline_and_grades_by_id(self, dis_id):
        action = ComplexUndoRedoAction()
        discipline = self.__disciplineRepository.search(Discipline(dis_id, ""))
        grades = self.__gradeRepository.get_all()
        for grade in grades:
            if grade.get_discipline() == discipline:
                self.__gradeRepository.remove(grade)
                grade_action = UndoRedoAction(self.__gradeRepository, self.__gradeRepository.add,
                                              self.__gradeRepository.remove, grade)
                action.add_action(grade_action)
        self.__disciplineRepository.remove(discipline)
        discipline_action = UndoRedoAction(self.__disciplineRepository, self.__disciplineRepository.add,
                                           self.__disciplineRepository.remove, discipline)
        action.add_action(discipline_action)
        self.__undoStack.push(action)
        self.__redoStack.clear()

    def statistics_students_failing(self):
        partial_grades = self.__gradeRepository.get_all()
        grades = []
        for grade in partial_grades:
            student = self.__studentRepository.search(Student(grade.get_student().get_stud_id(), ""))
            discipline = self.__disciplineRepository.search(Discipline(grade.get_discipline().get_dis_id(), ""))
            grades.append(Grade(student, discipline, grade.get_value()))
        students = {}
        for grade in grades:
            if not grade.get_student().get_stud_id() in students:
                students[grade.get_student().get_stud_id()] = []
            students[grade.get_student().get_stud_id()].append(grade.get_value())
        failing = []
        for item in students.items():
            stud_id = item[0]
            stud_name = self.__studentRepository.search(Student(stud_id, "")).get_stud_name()
            average = sum(item[1]) / len(item[1])
            if average < 5.0:
                fail_stud_dto = StudentDTO(stud_name, average)
                failing.append(fail_stud_dto)
        failing.sort(key=lambda x: x.get_average(), reverse=False)
        return failing[:]

    def statistics_students_best(self):
        partial_grades = self.__gradeRepository.get_all()
        grades = []
        for grade in partial_grades:
            student = self.__studentRepository.search(Student(grade.get_student().get_stud_id(), ""))
            discipline = self.__disciplineRepository.search(Discipline(grade.get_discipline().get_dis_id(), ""))
            grades.append(Grade(student, discipline, grade.get_value()))
        students = {}
        for grade in grades:
            if not grade.get_student().get_stud_id() in students:
                students[grade.get_student().get_stud_id()] = []
            students[grade.get_student().get_stud_id()].append(grade.get_value())
        best = []
        for item in students.items():
            stud_id = item[0]
            stud_name = self.__studentRepository.search(Student(stud_id, "")).get_stud_name()
            average = sum(item[1]) / len(item[1])
            best_stud = StudentDTO(stud_name, average)
            best.append(best_stud)
        best.sort(key=lambda x: x.get_average(), reverse=True)
        return best[:3]

    def statistics_disciplines(self):
        partial_grades = self.__gradeRepository.get_all()
        grades = []
        for grade in partial_grades:
            student = self.__studentRepository.search(Student(grade.get_student().get_stud_id(), ""))
            discipline = self.__disciplineRepository.search(Discipline(grade.get_discipline().get_dis_id(), ""))
            grades.append(Grade(student, discipline, grade.get_value()))
        disciplines = {}
        for grade in grades:
            if not grade.get_discipline().get_dis_id() in disciplines:
                disciplines[grade.get_discipline().get_dis_id()] = []
            disciplines[grade.get_discipline().get_dis_id()].append(grade.get_value())
        results = []
        for item in disciplines.items():
            dis_id = item[0]
            dis_name = self.__disciplineRepository.search(Discipline(dis_id, "")).get_dis_name()
            average = sum(item[1]) / len(item[1])
            dis_dto = DisciplineDTO(dis_name, average)
            results.append(dis_dto)
        results.sort(key=lambda x: x.get_average(), reverse=True)
        return results[:]

    def get_grades(self):
        grades = self.__gradeRepository.get_all()
        rez = []
        for grade in grades:
            student = self.__studentRepository.search(Student(grade.get_student().get_stud_id(), ""))
            discipline = self.__disciplineRepository.search(Discipline(grade.get_discipline().get_dis_id(), ""))
            rez.append(Grade(student, discipline, grade.get_value()))
        return rez


class UndoRedoService(object):

    def __init__(self, undoStack, redoStack):
        self.__undoStack = undoStack
        self.__redoStack = redoStack

    def undo(self):
        action = self.__undoStack.pop()
        action.execute()
        redo_action = action.get_opposite()
        self.__redoStack.push(redo_action)

    def redo(self):
        action = self.__redoStack.pop()
        action.execute()
        redo_action = action.get_opposite()
        self.__undoStack.push(redo_action)
