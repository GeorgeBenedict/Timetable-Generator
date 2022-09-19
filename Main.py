from Location import Location
from Module import Module
from ModuleOffering import ModuleOffering
from Schedule import Schedule
import os
 
def loadData(filename, mods, locs, table):
    global path
    filepath = path + "/" + filename

    try:
        file = open(filepath, "r")    
        modOffering = ModuleOffering(term="", mode="", module="")
        for line in file:
            if "Name" not in line:
                columns = line.split(",")

                name = columns[1]
                nameinfo = name.split("_")
                module = nameinfo[0]
                term = nameinfo[1]
                mode = nameinfo[2]
                modulecode = nameinfo[3]
                activity = nameinfo[4]

                modulename = columns[2].replace("SET ", "")
                scheduledate = columns[3]
                scheduleday = columns[4]
                sTime = columns[5]
                eTime = columns[6]
                dura = columns[7]
                room = columns[8]
                cap = columns[9]
                lecturer = columns[10]
                zone = columns[11].strip("\n")

                module = Module(modulecode, modulename)
                module = checkExistOrAppend(mods, module)

                location = Location(room, zone)
                location = checkExistOrAppend(locs, location)

                modOffering.term = term
                modOffering.modeOfStudy = mode
                modOffering.module = module
                #modOffering = checkExistOrAppend(terms, modOffering)

                modOffering.createSchedule(term, name, scheduledate, scheduleday, sTime, eTime, dura, cap, lecturer, location)
                
        table.append(modOffering)
                
        return

    except Exception as e:
        print (e)

def checkExistOrAppend(collection, item):
    for c in collection:
        if c.sameAs(item):
            return c
    collection.append(item)
    return item

# global path

def main():
    global path
    modules = []
    locations = []
    timetable = []

    print("\nWelcome \n")
    print(" n︵∩\n/     \ \n\ ˚ᴥ˚ /\n( (_) )\n(,,)(,,)\n")
    input("Press enter to continue...\n")

    userInput = 0

    while userInput != 99:
        print("\n  Main Menu")
        print("|---------------------------------------|")
        print("| What do you want to do?\t\t|\n|---------------------------------------|\n| (1)\tLoad data\t\t\t|\n| (2)\tList all modules\t\t|\n| (3)\tList all timetables\t\t|\n| (4)\tList schedule by module code\t|\n| (5)\tList schedule by lecturer\t|\n| (6)\tList schedule by location/zone\t|\n| (7)\tKeyword search\t\t\t|\n| (99)\tEXIT\t\t\t\t|\n|---------------------------------------|")
        userInput = int(input("\nEnter a number: "))         
        if userInput == 1:
            targetPath = input("Enter target folder containing dataset: ")
            path = targetPath
            print("\n")
            count = 0
            for root, folders, files in os.walk(targetPath):
                for file in files:
                    loadData(file, modules, locations, timetable)
                    # loadData(file, modules, offerings, locations, timetable)
                    count += 1

            print("{} dataset has been added.".format(str(count)))
            
        elif userInput == 2:
            print("\n")
            for m in modules:
                print(m)
               
        elif userInput == 3:
            print("\n")
            header = "{:<51}{:<31}{:<46}{:<21}{:<41}{}".format("Name", "Date", "Time", "Student Size", "Lecturer", "Location")
            headerLine = "{:<51}{:<31}{:<46}{:<21}{:<41}{}".format("----", "----", "----", "------------", "--------", "--------")
            print (header)
            print (headerLine)
            for t in timetable:
                for x in t.schedules:
                    print(x)

        elif userInput == 4:
            keywordSearch1 = input("Enter a module code (e.g. ISOG, DDMG): ")
            keyword1 = []
            for t in timetable:
                for x in t.schedules:
                    if keywordSearch1.lower() in x.activityType.lower():
                        keyword1.append(x)
            for variable in keyword1:
                print(variable)

        elif userInput == 5:
            keywordSearch2 = input("Enter a lecturer name: ")
            keyword2 = []
            for t in timetable:
                for x in t.schedules:
                    if keywordSearch2.lower() in x.lecturer.lower():
                        keyword2.append(x)
            for variable in keyword2:
                print(variable)
            
        elif userInput == 6:
            keywordSearch3 = input("Enter a location/zone name: ")
            keyword3 = []
            for t in timetable:
                for x in t.schedules:
                    if keywordSearch3.lower() in x.location.room.lower() or keywordSearch3.lower() in x.location.zone.lower():
                        keyword3.append(x)
            for variable in keyword3:
                print(variable)

        elif userInput == 7:
            keywordSearch = input("Enter keyword search: ")
            keyword = []
            for t in timetable:
                for x in t.schedules:
                    if keywordSearch.lower() in x.activityType.lower() or keywordSearch.lower() in x.date.lower() or keywordSearch.lower() in x.day.lower() or keywordSearch.lower() in x.startTime.lower() or keywordSearch.lower() in x.endTime.lower() or keywordSearch.lower() in x.duration.lower() or keywordSearch.lower() in x.capacity.lower() or keywordSearch.lower() in x.lecturer.lower() or keywordSearch.lower() in x.location.room.lower() or keywordSearch.lower() in x.location.zone.lower():
                        keyword.append(x)
            for variable in keyword:
                print(variable)

        
                
main()


