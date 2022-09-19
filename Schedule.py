from Location import Location

class Schedule:
    def __init__(self, act, actType, date, day, sTime, eTime, duration, cap, lec, loc):
        self.activity = act
        self.activityType = actType
        self.date = date
        self.day = day
        self.startTime = sTime
        self.endTime = eTime
        self.duration = duration + " hours)"
        self.capacity = cap
        self.lecturer = lec
        self.location = loc

    def __str__(self):
        info = "|{:<50}|{:<10}{:<20}|{:<5}-{:<5} ({:<20}\t|{:<20}|{:<40}|{}".format(self.activityType, self.date, self.day, self.startTime, self.endTime, self.duration,self.capacity, self.lecturer, self.location)
        return info


        # for i in self.activity:
        #     if i == ''or'a'or'b'or'c'or'd'or'e'or'f'or'g'or'h'or'i'or'j'or'k'or'l'or 'm'or'n'or'o'or'p'or'q'or'r'or's'or't'or'u'or'v'or'w'or'x'or'y'or'z'or'0'or'1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9'or'-'or'_':
        #         nameCount = nameCount + 1
        # for i in self.lecturer:
        #     if i == ''or'a'or'b'or'c'or'd'or'e'or'f'or'g'or'h'or'i'or'j'or'k'or'l'or 'm'or'n'or'o'or'p'or'q'or'r'or's'or't'or'u'or'v'or'w'or'x'or'y'or'z':
        #         count = count + 1
        # if "Lab" in self.activity and count < 15 :
        #     info = "{}\t\t{} ({})\t[{}-{}  ({} hours)]\t{} Students\t {}\t\t\t\t{}".format(self.activityType, self.date, self.day, self.startTime, self.endTime, self.duration,self.capacity, self.lecturer, self.location)
        #     return info
        
        # elif "Lab" in self.activity and count > 15 and count <22 :
        #     info = "{}\t\t{} ({})\t[{}-{}  ({} hours)]\t{} Students {}\t\t\t{}".format(self.activityType, self.date, self.day, self.startTime, self.endTime, self.duration,self.capacity, self.lecturer, self.location)
        #     return info
        
        # elif count > 15 and count < 22:
        #     info = "{}\t\t\t{} ({})\t[{}-{}  ({} hours)]\t{} Students {}\t\t\t{}".format(self.activityType, self.date, self.day, self.startTime, self.endTime, self.duration,self.capacity, self.lecturer, self.location)
        #     return info

        # elif "Lab" in self.activityType:
        #     info = "{}\t\t{} ({})\t[{}-{}  ({} hours)]\t{} Students {}\t{}".format(self.activityType, self.date, self.day, self.startTime, self.endTime, self.duration,self.capacity, self.lecturer, self.location)
        #     return info
        # elif count < 15:
        #     info = "{}\t\t\t{} ({})\t[{}-{}  ({} hours)]\t{} Students {}\t\t\t\t{}".format(self.activityType, self.date, self.day, self.startTime, self.endTime, self.duration,self.capacity, self.lecturer, self.location)
        #     return info
        # else:
        #     info = "{}\t\t\t{} ({})\t[{}-{}  ({} hours)]\t{} Students {}\t{}".format(self.activityType, self.date, self.day, self.startTime, self.endTime, self.duration,self.capacity, self.lecturer, self.location)
        #     return info
        
        
        # info = "{}-{}\t\t{} ({})\t[{}-{} ({} hours)]\t {}\t{}".format(self.activityType, self.activity, self.date, self.day, self.startTime, self.endTime, self.duration, self.lecturer, self.location)
        # return info

    # def __str__(self):
    #     info = "{}-{} on {} ({}) [{}-{} ({} hours)] by {} at {}".format(self.activityType, self.activity, self.date, self.day, self.startTime, self.endTime, self.duration, self.lecturer, self.location)
    #     return info

    # def sameAs(self, other):
    #     return self.activity == other.activity and self.activityType == other.activityType


