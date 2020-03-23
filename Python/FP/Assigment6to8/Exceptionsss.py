# Exceptions Module for Student Register Management
  
class StudentException(Exception):
    def __init__(self, message):
        super().__init__(message)

class DisciplineException(Exception):
    def __init__(self, message):
        super().__init__(message)

class GradeException(Exception):
    def __init__(self, message):
        super().__init__(message)