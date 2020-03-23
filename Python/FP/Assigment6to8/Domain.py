# Domanin Module for Students Register Management
  
class Student:
    def __init__(self, studentID, studentName):
        self.studentID = studentID
        self.studentName = studentName

class Discipline:
    def __init__(self, disciplineID, disciplineName):
        self.disciplineID = disciplineID
        self.disciplineName = disciplineName

class Grade():
    def __init__(self, disciplineID, studentID, gradeValue):
        self.disciplineID = disciplineID
        self.studentID = studentID
        self.gradeValue = gradeValue