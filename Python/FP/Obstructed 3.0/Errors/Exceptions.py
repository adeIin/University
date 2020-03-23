class UIError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class RepoError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
