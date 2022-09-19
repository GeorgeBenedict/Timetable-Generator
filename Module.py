class Module:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.courses = []

    def __str__(self):
        return "{}-{}".format(self.code, self.name.replace("(Group A)","").replace("(Group B)",""))

    def sameAs(self, other):
        return self.code == other.code



    # def sameAs(self, other):
    #     return self.code == other.code and self.name == other.name