import random
# list of courses and their difficulty multipliers
courseList = {"English":["AP Lit", "Eng 12"], "Math":["Multivar", "Calc BC", "Calc AB", "Precalc"], 
           "Social Science":["Gov/Econ"], "Art:":["Band", "Orchestra", "Digital Imaging", "Ceramics"], 
           "Electives":["AP Physics 1", "AP Physics C", "AP Stats", "AP Chem", "AP Bio", "AP Human Geo", "APES", "TA"] }

difficulty = {"AP Lit":1.07, "Eng 12":0.97, 
                  "Multivar":1.07, "Calc BC":1.07, "Calc AB":1.05, "Precalc":0.98,
                  "Gov/Econ":1, "Band": 0.97, "Orchestra":0.97, "Digital Imaging":0.97, "Ceramics":0.97,
                  "AP Physics 1":1.05, "AP Physics C":1.07, "AP Stats":1.04, "AP Chem":1.04, "AP Bio":1.04, "AP Human Geo":1.04, "APES":1.04, "TA":0.97}

# extracurricular list and their daily hour consumption
extracurriculars = {"Underwater Tennis":4, "Picket Fence Long Jump":2, "Blindfold Lacrosse":4, "Sky-high Badminton":3, "Underwater Basket Weaving":1}
ECList = ["Underwater Tennis", "Picket Fence Long Jump", "Blindfold Lacrosse", "Sky-high Badminton", "Underwater Basket Weaving"]

def chooseNum(low, up):
    validSelection = False
    while not validSelection:
        sel = input()
        if sel.isdigit() and low <= int(sel) <= up:
            print()
            return int(sel)
        else:
            print("Invalid input. Try again.")

def calculateDifficulty(schedule):
    total = 0.0
    for course in schedule:
        total += difficulty[course]
    return total / len(schedule)

# shorten double so that 3.456789 becomes 3.46
def truncateGPA(num):
    num *= 100
    
    # check next decimal to see if rounding is necessary
    if ((((num * 10) // 1) % 10) >= 5):
        num += 1
    num //= 1
    num /= 100
    return num