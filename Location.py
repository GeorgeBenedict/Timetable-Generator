class Location:
    def __init__(self, room, zone):
        self.room = room
        self.zone = zone
    
    def __str__(self):
        return "{} ({})".format(self.room, self.zone)

    def sameAs(self, other):
        return self.room == other.room and self.zone == other.zone