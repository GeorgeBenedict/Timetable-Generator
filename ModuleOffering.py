from Module import Module
from Location import Location
from Schedule import Schedule

class ModuleOffering:
    def __init__(self, term, mode, module):
        self.term = term
        self.modeOfStudy = mode
        self.module = module
        self.schedules = []

    def __str__(self):
        return "{} for term {} ({})".format(self.module.name, self.term, self.modeOfStudy)

    def createSchedule(self, act, actType, date, day, sTime, eTime, dura, cap, lec, location):
        schedule = Schedule(act, actType, date, day, sTime, eTime, dura, cap, lec, location)
        self.schedules.append(schedule)

    def sameAs(self, other):
        return self.term == other.term and self.modeOfStudy == other.modeOfStudy and self.module.code == other.module.code

    # def summary(self):
    #     print(self)
    #     for sch in self.schedules:
    #         print(sch)

