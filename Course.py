from Module import Module

class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.modules = []