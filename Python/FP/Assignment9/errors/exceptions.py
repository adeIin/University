class RepositoryError(Exception):
    def __init__(self, message):
        super().__init__(message)


class UndoRedoError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
