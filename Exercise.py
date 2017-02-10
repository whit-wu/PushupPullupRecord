import os
import csv
import time

class Workouts(object):



    # Has user perform Day 1 workouts
    def DayOneWorkouts(self):

        pushupreps = []
        chinupreps = []

        os.system('cls')
        print("Day One Workouts"
              "\nWorkouts for the day: "
              "\n   Feet Elevated Pushup"
              "\n   Chinup")
        print("Press Enter to begin workouts...")
        input()

        # with open('Workouts.csv', 'w') as csvfile:
        #     CurrentDateWriter = csv.writer(csvfile)
        #     CurrentDateWriter.writerow(["Day One Workouts", time.strftime("%Y-%m-%d")])
            # CurrentDateWriter.writerow(time.strftime("%H:%M:%S"))
        #loop to keep track of sets that need to be performed by user
        for i in range(5):
            os.system('cls')
            print("Feet Elevated Pushup"
                "\nSets: 5 Reps: As many as possible"
                "\nPlace your feet on a bench or other elevated surface and get into "
                "\npushup position with your hands shoulder-width apart. Brace your core "
                "\nand lower your body until your chest is just above the floor.")
            print("Enter reps for set " + str(i + 1) + ":")
            #firstWorkoutRep = input()
            pushupreps.append(input())

            os.system('cls')
            print("Chinup"
                  "\nSets: 5 Reps: As many as possible"
                  "\nHang from a chinup bar with hands shoulder-width apart and palms"
                  "\nfacing you. Pull yourself up until your chin is over the bar.")
            print("Enter reps for set " + str(i + 1) + ":")
            #secondWorkoutRep = input()
            chinupreps.append(input())
        with open('Workouts.csv', 'a', newline='') as csvfile:
            WorkoutWriter = csv.writer(csvfile, delimiter=',')
            #RepWriter = csv.writer(csvfile, delimiter=',')
            WorkoutWriter.writerow(["Day One Workouts", time.strftime("%Y-%m-%d")])
            WorkoutWriter.writerow(["Feet Elevated Pushup", "(5:AMRAP)", '', 'Chinup', '(5:AMRAP)'])
            for i in range(len(pushupreps)):
                WorkoutWriter.writerow(['Set ' + str(i+1), pushupreps[i], '', 'Set ' + str(i+1), chinupreps[i]])
            WorkoutWriter.writerow('')
            WorkoutWriter.writerow('')


    # Has user perform Day 2 workouts
    def DayTwoWorkouts(self):
        print("Day Two Workouts")

    # Has user perform Day 3 workouts
    def DayThreeWorkouts(self):
        print("Day Three Workouts")

    # Has user perform Day 4 workouts
    def DayFourWorkouts(self):
        print("Day Four Workouts")

    # Has user perform Day 5 workouts
    def DayFiveWorkouts(self):
        print("Day Five Workouts")

    # Reads line on file to determine what day it is.
    # Day determines the workout user will do.
    def ReadDayFile(self):
        f = open('DayFile.txt', 'r')
        # print(f)
        contents = f.read()
        print(contents[4])
        if contents[4] == '1':
            #do the day 1 workouts
            print("this works")
            self.DayOneWorkouts()
        elif contents[4] == '2':
            #do the day 2 workouts
            print("this works")
            self.DayTwoWorkouts()
        elif contents[4] == '3':
            #do the day 3 workouts
            print("this works")
            self.DayThreeWorkouts()
        elif contents[4] == '4':
            #do the day 4 workouts
            print("this works")
            self.DayFourWorkouts()
        elif contents[4] == '5':
            #do the day 5 workouts
            print("this works")
            self.DayFiveWorkouts()

