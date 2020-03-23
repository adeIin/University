from errors.exceptions import RepositoryError, ValidationError, UndoRedoError


class Console(object):
    
    def __init__(self, srvStud, srvDis, srvGrad, srvUndoRedo):
        self.__studentService = srvStud
        self.__disciplineService = srvDis
        self.__gradeService = srvGrad
        self.__undoRedoService = srvUndoRedo
    
    def __ui_add_student(self):
        stud_id = int(input("Insert student id:\n>>>"))
        stud_name = input("Insert student name:\n>>>")
        self.__studentService.add_student(stud_id, stud_name)
        print("\nStudent successfully added!\n")
    
    def __ui_add_discipline(self):
        dis_id = int(input("Insert discipline id:\n>>>"))
        dis_name = input("Insert discipline name:\n>>>")
        self.__disciplineService.add_discipline(dis_id, dis_name)
        print("\nDiscipline successfully added!\n")
    
    def __ui_add_grade(self):
        stud_id = int(input("Insert student id:\n>>>"))
        dis_id = int(input("Insert discipline id:\n>>>"))
        grad_val = float(input("Insert grade value:\n>>>"))
        self.__gradeService.add_grade(stud_id, dis_id, grad_val)
        print("\nGrade successfully added!\n")
    
    def __ui_print_students(self):
        students = self.__studentService.get_students()
        for student in students:
            print("***\n", student)
        print("***\n")
    
    def __ui_print_disciplines(self):
        disciplines = self.__disciplineService.get_disciplines()
        for discipline in disciplines:
            print("***\n", discipline)
        print("***\n")
    
    def __ui_print_grades(self):
        grades = self.__gradeService.get_grades()
        for grade in grades:
            print("***\n",grade)
        print("***\n")

    def __ui_remove_student(self):
        stud_id = int(input("Insert student id:\n>>>"))
        self.__gradeService.remove_student_and_grades_by_id(stud_id)
        print("\nStudent successfully removed!\nStudent's grades successfully removed!\n")
    
    def __ui_remove_discipline(self):
        dis_id = int(input("Insert discipline id:\n>>>"))
        self.__gradeService.remove_discipline_and_grades_by_id(dis_id)
        print("\nDiscipline successfully removed!\nStudents successfully removed!\nDiscipline's grades successfully "
              "removed!\n")
    
    def __ui_update_student_id(self):
        old_stud_id = int(input("Insert old student id:\n>>>"))
        new_stud_id = int(input("Insert new student id:\n>>>"))
        self.__studentService.update_student_id(old_stud_id, new_stud_id)
        print("\nStudent id successfully updated!\n")
    
    def __ui_update_student_name(self):
        stud_id = int(input("Insert student id:\n>>>"))
        new_stud_name = input("Insert new student name:\n>>>")
        self.__studentService.update_student_name(stud_id, new_stud_name)
        print("\nStudent name successfully updated!\n")
    
    def __ui_update_discipline_id(self):
        old_dis_id = int(input("Insert old discipline id:\n>>>"))
        new_dis_id = int(input("Insert new discipline id:\n>>>"))
        self.__disciplineService.update_discipline_id(old_dis_id, new_dis_id)
        print("\nDiscipline id successfully updated!\n")
    
    def __ui_update_discipline_name(self):
        dis_id = int(input("Insert discipline id:\n>>>"))
        new_dis_name = input("Insert new discipline name:\n>>>")
        self.__disciplineService.update_discipline_name(dis_id, new_dis_name)
        print("\nDiscipline name successfully updated!\n")
    
    def __ui_search_student_name(self):
        stud_name = input("Insert student name:\n>>>")
        matched_students = self.__studentService.search_student_name(stud_name)
        print("\nStudents found:")
        for student in matched_students:
            print("***\n", student)
        print("***\n")
     
    def __ui_search_student_id(self):
        stud_id = int(input("Insert student id:\n>>>"))
        student = self.__studentService.search_student_id(stud_id)
        print("\nStudent found:\n", student, "\n")
    
    def __ui_search_discipline_name(self):
        dis_name = input("Insert discipline name:\n>>>")
        matched_disciplines = self.__disciplineService.search_discipline_name(dis_name)
        print("\nDisciplines found:")
        for discipline in matched_disciplines:
            print("***\n", discipline)
        print("***\n")
    
    def __ui_search_discipline_id(self):
        dis_id = int(input("Insert discipline id:\n>>>"))
        discipline = self.__disciplineService.search_discipline_id(dis_id)
        print("\nDiscipline found:\n", discipline, "\n")
    
    def __ui_statistics_students_failing(self):
        students_failing = self.__gradeService.statistics_students_failing()
        print("Failing students are:")
        for student in students_failing:
            print("***\n", student)
        print("***\n")
    
    def __ui_statistics_students_best(self):
        students_best = self.__gradeService.statistics_students_best()
        print("Best 3 students are:")
        for student in students_best:
            print("***\n", student)
        print("***\n")
    
    def __ui_statistics_disciplines(self):
        disciplines = self.__gradeService.statistics_disciplines()
        print("Disciplines statistics:")
        for discipline in disciplines:
            print("***\n", discipline)
        print("***\n")
    
    def __ui_undo(self):
        self.__undoRedoService.undo()
        print("\nSuccessful undo!\n")
    
    def __ui_redo(self):
        self.__undoRedoService.redo()
        print("\nSuccessful redo!\n")
    
    def run(self):
        
        commands = {
            '1':  self.__ui_add_student,
            '2':  self.__ui_add_discipline,
            '3':  self.__ui_add_grade,
            '4':  self.__ui_print_students,
            '5':  self.__ui_print_disciplines,
            '6':  self.__ui_print_grades,
            '7':  self.__ui_remove_student,
            '8':  self.__ui_remove_discipline,
            '9':  self.__ui_update_student_id,
            '10': self.__ui_update_student_name,
            '11': self.__ui_update_discipline_id,
            '12': self.__ui_update_discipline_name,
            '13': self.__ui_search_student_name,
            '14': self.__ui_search_student_id,
            '15': self.__ui_search_discipline_name,
            '16': self.__ui_search_discipline_id,
            '17': self.__ui_statistics_students_failing,
            '18': self.__ui_statistics_students_best,
            '19': self.__ui_statistics_disciplines,
            '20': self.__ui_undo,
            '21': self.__ui_redo
            }
        
        while True:
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
            print("           (11) to update discipline ID.")
            print("           (12) to update discipline name.")
            print("           (13) to search a student by name.")
            print("           (14) to search a student by ID.")
            print("           (15) to search a discipline by name.")
            print("           (16) to search a discipline by ID.")
            print("           (17) to view statistics for failing students.")
            print("           (18) to view statistics for best students.")
            print("           (19) to view statistics for disciplines.")
            print("           (20) to undo.")
            print("           (21) to redo.")
            print("           (0) to exit.\n")
            
            cmd = input("Insert command: \n>>>")
            print("")
            if cmd == '0':
                print("Program closed.")
                return
            if cmd not in commands:
                print("Invalid command!\n")
            if cmd in commands:
                try:
                    commands[cmd]()
                except ValueError as ve:
                    print("\nUser Interface error:\n---> " + str(ve) + "\n")
                except ValidationError as vale:
                    print("\nValidation error:\n---> " + str(vale) + "\n")
                except RepositoryError as re:
                    print("\nRepository error:\n---> " + str(re) + "\n")
                except UndoRedoError as ure:
                    print("\nUndo/Redo error:\n---> " + str(ure) + "\n")
        


