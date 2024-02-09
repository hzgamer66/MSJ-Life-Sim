from Student import Student
from functions import *


def runSim():
    print("Welcome to MSJ Life Simulator! You a are a current student at the beginning of their senior year with a very clingy girlfriend.\n")
    print("\nSelect your courses.")
    # select schedule + ec
    schedule = chooseCourses(courseList)
    ec = ECList[chooseEC()]
    student = Student(schedule, ec)

    # run each week!
    while student.week <= 36:
        student.doWeek()


# list and choose the ec's
def chooseEC():
    options = "Choose your extracurricular by picking ONE from the following list: \n"
    for i in range(0, len(ECList)):
        options += str(i + 1) + ". " + ECList[i] + " | "
    options = options[0:-3]
    print(options)
    return chooseNum(1, 5)

# list and choose the courses
def chooseCourses(courseList):
    finalCourses = []
    for item in courseList:
        # single choice categories
        if item != "Electives":
            # list each option
            options = "\nChoose ONE from the following " + item + " courses by typing the corresponding number:\n"
            for i in range(1, len(courseList[item]) + 1):
                options += str(i) + ". " + courseList[item][i-1] + " | "
            options = options[0:-3]
            print(options)
            
            # select a valid number
            validSelection = False
            while not validSelection:
                sel = input()
                if sel.isdigit() and 1 <= int(sel) <= len(courseList[item]) + 1:
                    finalCourses.append(courseList[item][int(sel) - 1])
                    validSelection = True
                else:
                    print("Invalid input. Try again.")

        # electives: multiple choices
        else:
            options = "\nChoose TWO from the following " + item + " courses by typing the corresponding two numbers with a space in between (i.e \"1 2\"):\n"
            for i in range(1, len(courseList[item]) + 1):
                options += str(i) + ". " + courseList[item][i-1] + " | "
            options = options[0:-3]
            print(options + "\n")
            
            validSelection = False
            while not validSelection:
                sel = input()
                if len(sel) >= 3:
                    # convert "1 2" --> "1" and "2"
                    first = sel[0:1]
                    second = sel[-1:]
                    if first.isdigit() and second.isdigit() and not (first == second) and 1 <= int(first) <= len(courseList[item]) + 1 and 1 <= int(second) <= len(courseList[item]) + 1:
                        finalCourses.append(courseList[item][int(first) - 1])
                        finalCourses.append(courseList[item][int(second) - 1])
                        validSelection = True
                        print()
                else:
                    print("Invalid input. Try again.")
    return finalCourses
                
        

            


def main():
    running = True
    while running:
        runSim()
        print("\nWould you like to play again? y/n")
        valid = False
        while not valid:
            response = input
            if response == "y":
                valid = True
            if response == "n":
                valid = True
                running = False

main()


