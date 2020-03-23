from errors.exceptions import ValidationError


class ValidateStudent:
    
    def validate_student(self, student):
        errors = ""
        if student.get_stud_id() < 0:
            errors += "Invalid student id!\n"
        if student.get_stud_name() == "":
            errors += "Invalid student name!\n"
        if len(errors) > 0:
            raise ValidationError(errors)


class ValidateDiscipline:
    
    def validate_discipline(self, discipline):
        errors = ""
        if discipline.get_dis_id() < 0:
            errors += "Invalid discipline id!\n"
        if discipline.get_dis_name() == "":
            errors += "Invalid discipline name!\n"
        if len(errors) > 0:
            raise ValidationError(errors)


class ValidateGrade:
    
    def validate_grade(self, grade):
        errors = ""
        if grade.get_value() < 1 or grade.get_value() > 10.0:
            errors += "Invalid grade value!\n"
        if len(errors) > 0:
            raise ValidationError(errors)
