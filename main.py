from Student import Student
courseList = {"English":["AP Lit", "Eng 12"], "Math":["Multivar", "Calc BC", "Calc AB", "Precalc"], 
           "Social Science":["Gov/Econ"], "Art:":["Band", "Orchestra", "Digital Imaging", "Ceramics"], 
           "Electives":["AP Physics 1", "AP Physics C", "AP Stats", "AP Chem", "AP Bio", "AP Human Geo", "APES", "TA"] }

difficulty = {"AP Lit":1.05, "Eng 12":0.95, 
                  "Multivar":1.05, "Calc BC":1.05, "Calc AB":1.02, "Precalc":0.98,
                  "Gov/Econ":1, "Band": 0.97, "Orchestra":0.97, "Digital Imaging":0.97, "Ceramics":0.97,
                  "AP Physics 1":1.03, "AP Physics C":1.05, "AP Stats":1.02, "AP Chem":1.03, "AP Bio":1.03, "AP Human Geo":1.03, "APES":1.03, "TA":0.97}
extracurriculars = {"Underwater Tennis":5, "Picket Fence Long Jump":3, "Blindfold Lacrosse":5, "Sky-high Badminton":4, "Underwater Basket Weaving":0}
ECList = ["Underwater Tennis", "Picket Fence Long Jump", "Blindfold Lacrosse", "Sky-high Badminton", "Underwater Basket Weaving"]

def main():
    print("Welcome to MSJ Life Simulator! You a are a current student at the beginning of their senior year.\nWhile you currently have a very clingy girlfriend, you are trying to have a social life while still keeping up with grades and college apps. ")
    print("\nSelect your courses.")
    schedule = chooseCourses(courseList)
    ec = chooseEC()
    student = Student(schedule, ec)

    while student.week <= 36:
        print("Week: " + str(student.week) + " | Current GPA: " + str(student.GPA))
        student.doWeek()



def chooseNum(nums):
    validSelection = False
    while not validSelection:
        sel = input()
        if sel.isdigit() and 1 <= int(sel) <= nums:
            print()
            return int(sel)
        else:
            print("Invalid input. Try again.")

def chooseEC():
    options = "Choose your extracurricular by picking ONE from the following list: \n"
    for i in range(0, len(ECList)):
        options += str(i + 1) + ". " + ECList[i] + " | "
    options = options[0:-3]
    print(options)
    return chooseNum(5)


def chooseCourses(courseList):
    finalCourses = []
    for item in courseList:
        if item != "Electives":
            options = "\nChoose ONE from the following " + item + " courses by typing the corresponding number:\n"
            for i in range(1, len(courseList[item]) + 1):
                options += str(i) + ". " + courseList[item][i-1] + " | "
            options = options[0:-3]
            print(options)
            
            validSelection = False
            while not validSelection:
                sel = input()
                if sel.isdigit() and 1 <= int(sel) <= len(courseList[item]) + 1:
                    finalCourses.append(courseList[item][int(sel) - 1])
                    validSelection = True
                else:
                    print("Invalid input. Try again.")
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
                
        

            


main()


