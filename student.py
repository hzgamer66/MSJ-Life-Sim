from functions import *

# number of tests each week ([week 1, week 2, ... week 36]). used in grade calculations.
numTests = [0.0, 1.0, 2.0, 3.0, 3.0, 4.0, 2.0, 4.0, 1.0, 1.0, 2.0, 3.0, 4.0, 2.0, 5.0, 3.0, 2.0, 4.0, 0.0, 1.0, 2.0, 1.0, 3.0, 5.0, 2.0, 3.0, 2.0, 4.0, 4.0, 2.0, 1.0, 2.0, 2.0, 4.0, 3.0, 5.0]

class Student:
    def __init__(self, schedule, ec):
        self.GPA = 4.0
        self.schedule = schedule
        self.ec = ec
        self.ecHours = extracurriculars[ec]
        self.week = 1
        self.quarter = 1
        self.relationship = True

        self.luck = 1
        self.loveScore = 75
        self.hygine = 90
        self.social = 80
        self.ecrank = 1

        self.studyHours = 0
        self.weekPerformance = 1

        self.totalGPA = 0
        self.weightedDifficulty = calculateDifficulty(schedule)
        
    def doWeek(self):
        print("\nWeek: " + str(self.week) + " | Current GPA: " + str(self.GPA))
        tests = numTests[self.week - 1]
        
        print("You have " + str(tests) + " tests this week. How many hours would you like to study each day? (Int between 1 and 6)")
        self.studyHours = chooseNum(1, 6)
        self.weekPerformance = 1

        # run event based on hours left
        self.events(12 - self.studyHours - self.ecHours)

        # update your grade
        self.calculateWeek()
        self.advanceWeek()



    def calculateWeek(self):
        multiplier = ((-self.weightedDifficulty + 1.0) + (self.weekPerformance - 1.0) + (1 - ((numTests[self.week - 1] + 1)/self.studyHours))) / 30

        # gpa balancing
        if -0.05 < multiplier < 0.05:
            self.GPA += multiplier
        elif multiplier > 0.1:
            self.GPA += 0.05
        else:
            self.GPA -= 0.05

        # rng cuz grades are just like that sometimes
        self.GPA += .01 * random.randint(0, 2)
        self.GPA -= .01 * random.randint(0, 2)

        if self.GPA > 4.0: self.GPA = 4.0
        self.GPA = truncateGPA(self.GPA)
        

    def advanceWeek(self):
        if self.week == 9 or self.week == 27:
            print("Quarter " + str(self.week / 9)  + " has ended. Lets check how you're doing!")
            print("GPA: " + str(self.GPA))
            print("Relationship score: " + str(self.loveScore) + "/100")
            print("Social score: " + str(self.social) + "/100")
            print("Your extracurricular rank: " + str(self.ecrank) + "/50")
            if self.loveScore < 60: print("Your girlfriend is thinking of breaking up with you. Keep her happy!")
            
        if self.week == 18:
            print("First semester has now ended.")
            print("GPA: " + str(self.GPA))
            print("Relationship score: " + str(self.loveScore) + "/100")
            print("Social score: " + str(self.social) + "/100")
            print("Your extracurricular rank: " + str(self.ecrank) + "/50")
            if self.loveScore < 60: print("Your girlfriend is thinking of breaking up with you. Keep her happy!")
        
        if self.week == 36:
            print("Second semester has now ended.")
            print("GPA: " + str(self.GPA))
            print("Relationship score: " + str(self.loveScore) + "/100")
            print("Social score: " + str(self.social) + "/100")
            print("Your extracurricular rank: " + str(self.ecrank) + "/50")

            college = "You ended up going to college at "
            collegeScore = (self.GPA/4.0 + (1.0 - (self.ecrank / 50))) / 2
            if collegeScore > 0.95: college += "a prestigious private school with full scholarship!"
            elif collegeScore > 0.90: college += "a prestigious private school!"
            elif collegeScore > 0.80: college += "a good high-quality public school!"
            elif collegeScore > 0.7: college += "a mid public school."
            else: college += "your local safety school."
            
            print(college)


            if self.loveScore < 60: print("Your girlfriend broke up with you as a graduation present :(")
            else: print("You managed to keep your girlfriend happy! Good job!")
    
        self.week += 1

    # depending on how many hours you're studying and your extracurriculars, you will get different events.
    def events(self, hours):
        # randomly select one of 3 events in each 
        seed = random.randint(1, 3)

        # busy schedule!
        if hours <= 3:
            if (seed == 1):
                print("Looks like a busy week. Would you like to take a long bath to relax instead of studying? | 1. Yes | 2. No |")
                if chooseNum(1, 2) == 1:
                    self.hygine += random.randint(6, 11)
                    self.weekPerformance = 0.92
                else:
                    self.hygine -= random.randint(6, 11)
                    self.weekPerformance = 1.02
            elif seed == 2:
                print("Your girlfriend keeps bugging you. Do you entertain her and text back even though you're busy studying? | 1. Yes | 2. No |")
                if chooseNum(1, 2) == 1:
                    self.loveScore += random.randint(5, 10)
                    self.weekPerformance = 0.9
                else:
                    self.loveScore -= random.randint(4, 12)
                    self.weekPerformance = 1.08
            else:
                print("Do you skip a practice or extracurricular meeting to study for this week's hectic schedule? | 1. Yes | 2. No |")
                if chooseNum(1, 2) == 2:
                    self.ecrank += random.randint(1, 3)
                    self.weekPerformance = 0.9
                else:
                    self.weekPerformance = 1.08
                    self.ecrank -= random.randint(1, 2)
                    self.social -= random.randint(3, 9)

            self.ecrank += random.randint(1, 3)
        
        # doing alright.
        elif 3 < hours <= 6:
            if (seed == 1):
                print("Your girlfriend wants to go out on a date, but you have extra practices/extracurricular meetings. Should you | 1. go on the date, or | 2. go to practice?")
                if chooseNum(1, 2) == 1:
                    self.loveScore += random.randint(5, 10)
                    self.ecrank += random.randint(1, 3)
                else:
                    self.loveScore -= random.randint(4, 12)
                    self.ecrank -= random.randint(1, 2)
                    self.hygine -= random.randint(2, 5)
                    self.social -= random.randint(3, 9)
            elif (seed == 2):
                print("Your friends are holding a study session! Do you go? | 1. Yes | 2. No |")
                if (chooseNum(1, 2) == 1):
                    self.weekPerformance = 1.1
                    self.loveScore -= random.randint(5, 10)
                    self.social += random.randint(5, 9)
                else:
                    self.loveScore += random.randint(7, 12)
                    self.social -= random.randint(5, 9)
            else:
                print("You're choosing groups for a group project. Do you join the smart kids, your friends, or your girlfriend? | 1. Smart kids | 2. Friends | 3. GF |")
                sel = chooseNum(1, 3)
                if sel == 1:
                    self.social -= random.randint(4, 8)
                    self.loveScore -= random.randint(4, 8)
                    self.weekPerformance = 1.14
                elif sel == 2:
                    self.social -= random.randint(4, 10)
                    self.loveScore += random.randint(5, 11)
                    self.weekPerformance = 0.88
                else:
                    self.social += random.randint(4, 10)
                    self.loveScore -= random.randint(4, 9)
                    self.weekPerformance = 0.95
        
        # hella free time
        else:
            if (seed == 1):
                print("This weekend, do you watch a movie with your friends, your girlfriend, or do you chill at home and play video games? | 1. Friends | 2. GF | 3. Stay at home |")
                sel = chooseNum(1, 3)
                if sel == 1:
                    self.social += random.randint(7, 11)
                    self.loveScore -= random.randint(4, 9)
                elif sel == 2:
                    self.social -= random.randint(4, 10)
                    self.loveScore += random.randint(5, 11)
                else:
                    self.social -= random.randint(4, 10)
                    self.loveScore -= random.randint(4, 9)
            elif seed == 2:
                print("A club is asking you to stay afterschool a few days this week to prepare for an event. Do you help? | 1. Yes | 2. No |")
                if (chooseNum(1, 2) == 1):
                    self.weekPerformance = 0.95
                    self.social += random.randint(4, 10)
                    self.ecrank -= random.randint(1, 2)
                else:
                    self.weekPerformance = 1.02
                    self.social -= random.randint(4, 10)
            else:
                print("You have a long term project due soon. Do you start on it while you have the time, or do you procrastinate? | 1. Start it | 2. Procrastinate |")
                if (chooseNum(1, 2) == 1):
                    self.weekPerformance = 1.1
                    self.social -= random.randint(4, 6)
                    self.ecrank += 1
                    self.loveScore -= random.randint(3, 6)
                else:
                    self.weekPerformance = 0.96
                    self.social += random.randint(4, 10)
                    self.loveScore += random.randint(3, 9)
                    self.ecrank -= 1

        if self.loveScore > 100: self.loveScore = 100
        if self.hygine > 100: self.hygine = 100
        if self.ecrank < 1: self.ecrank = 1
        if self.ecrank > 50: self.ecrank = 50

