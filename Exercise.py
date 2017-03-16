import os
import csv
import time
from WriteData import WriteData

class Workouts(object):



    # Has user perform Day 1 workouts
    def DayOneWorkouts(self):


        workOut1Message = "Feet Elevated Pushup" + "\nSets: 5 Reps: As many as possible" \
                          + "\nPlace your feet on a bench or other elevated surface and get into " \
                          + "\npushup position with your hands shoulder-width apart. Brace your core " \
                          + "\nand lower your body until your chest is just above the floor."

        workOut2Message = "Chinup" + "\nSets: 5 Reps: As many as possible"\
                          + "\nHang from a chinup bar with hands shoulder-width apart and palms facing you. " + \
                          "\nPull yourself up until your chin is over the bar."

        workoutDay = 1

        workout1 = "Feet Elevated Pushup"
        workout1Sets = "(5:AMRAP)"

        workout2 = "Chinup"
        workout2Sets = "(5:AMRAP)"

        os.system('cls')
        print("Day One Workouts"
              "\nWorkouts for the day: "
              "\n   Feet Elevated Pushup"
              "\n   Chinup")
        print("Press Enter to begin workouts...")
        input()
        dataToWrite = WriteData()
        dataToWrite.CaptureWorkoutData(5, workOut1Message, workOut2Message, workoutDay, workout1, workout2, workout1Sets, workout2Sets)





    # Has user perform Day 2 workouts
    def DayTwoWorkouts(self):
        print("Day Two Workouts")
        workout1Message = "Neutral Grip Chinup " "\nSets: 4 Reps: 4 1.5 reps " \
                          + "\nUse a chinup bar with parallel handles, or hook a V-grip bar over a" \
                          + "\nstraight chinup bar. Hang from the bar and pull yourself up until your chin is over it." \
                          + "\nHold for a second, then lower yourself halfway. Come back up, then lower yourself " \
                          + "\nto a full hang again. That’s one full “1.5” rep."

        workout2Message = "Close-Grip Pushup" "\nSets: 4 Reps: 20-25"\
                          + "\nGet into pushup position and bring your hands inside shoulder width. " \
                          + "\nKeep your core braced and perform a pushup."

        workoutDay = 2

        workout1 = "Neutral Grip Chinup"
        workout2 = "Close-Grip Pushup"

        workout1Sets = "(4: 4 x 1.5)"
        workout2Sets = "(4:20-25)"

        dataToWrite = WriteData()
        dataToWrite.CaptureWorkoutData(4, workout1Message, workout2Message, workoutDay, workout1, workout2, workout1Sets, workout2Sets)

    # Has user perform Day 3 workouts
    def DayThreeWorkouts(self):
        print("Day Three Workouts")
        workout1Message = "Pushup \nSets: 3 Countdown from 6" \
                          + "\nPerform six pushups, then lower your body into the bottom position so your " \
                          + "\nchest is just above the floor. Hold for six seconds, then perform five more pushups " \
                          + "\nfollowed by a five-second hold in the bottom position. Continue counting down, "\
                          + "\nalternating reps and static holds, until you reach one rep and a one-second hold."

        workout2Message = "Sternum Chinup \nSets: 3 Reps: AMRAP" \
                          + "\nHang from the chinup bar with hands shoulder-width apart and palms facing" \
                          + "\nyou. Lean back and pull yourself up, aiming to touch your lower chest to the bar."

        workoutDay = 3

        workout1 = "Pushup"
        workout2 = "Sternum Chinup"

        workout1Sets = "(3: Count down from 6)"
        workout2Sets = "(3:AMRAP)"
        dataToWrite = WriteData()
        dataToWrite.CaptureWorkoutData(3, workout1Message, workout2Message, workoutDay, workout1, workout2, workout1Sets, workout2Sets)

    # Has user perform Day 4 workouts
    def DayFourWorkouts(self):
        print("Day Four Workouts")
        workout1Message = "Pullup \nSets: 6 Reps: 5" \
                          + "\nHang from the bar with hands outside shoulder width and palms facing away from" \
                          + " you. Pull yourself up until your chin is over the bar."
        workout2Message = "One-Leg Pushup\nSets: 6 Reps: 10 per leg" + "\nGet into pushup position and raise one leg behind you. Keep it "\
                          + "\nelevated while you perform 10 pushups. Lower the leg, then raise the other one and "\
                          + "perform another 10 pushup"
        workoutDay = 4

        workout1 = "Pullup"
        workout2 = "One-Leg Pushup"

        workout1Sets = "(6:5)"
        workout2Sets = "(6: 10 per leg)"

        dataToWrite = WriteData()
        dataToWrite.CaptureWorkoutData(6, workout1Message, workout2Message, workoutDay, workout1, workout2, workout1Sets, workout2Sets)


    # Reads line on file to determine what day it is.
    # Day determines the workout user will do.
    def ReadDayFile(self):
        f = open('DayFile.txt', 'r')
        # print(f)
        contents = f.read()
        #print(contents[4])
        if contents[0] == '1':
            #do the day 1 workouts
            #print("this works")
            self.DayOneWorkouts()
        elif contents[0] == '2':
            #do the day 2 workouts
            #print("this works")
            self.DayTwoWorkouts()
        elif contents[0] == '3':
            #do the day 3 workouts
            #print("this works")
            self.DayThreeWorkouts()
        elif contents[0] == '4':
            #do the day 4 workouts
            #print("this works")
            self.DayFourWorkouts()
        else:
            print("Value in DayFile.txt not recognized.  Please open the file and verify it is a value between 1 and 4")
            return -1


