import os
import csv
import time


class WriteData(object):

    nextDay = 0

    # code to record reps that will be written to csv file
    def CaptureWorkoutData(self, setNum, workout1Message, workout2Message, workoutDay, workout1, workout2, workout1Sets, workout2Sets):
        workout1Reps = []
        workout2Reps = []
        workoutDayToWrite = workoutDay
        for i in range(setNum):
            print(workout1Message)
            print("Enter reps for set " + str(i + 1) + ":")
            workout1Reps.append(input())
            os.system('cls')
            print(workout2Message)
            print("Enter reps for set " + str(i + 1) + ":")
            workout2Reps.append(input())
        self.WriteToFile(workout1Reps, workout2Reps, workoutDayToWrite, setNum, workout1, workout2, workout1Sets, workout2Sets)

    # Code to write workout data to a csv file.  Also changes contents of DayFile.txt for next workout session.
    def WriteToFile(self, workout1Stats, workout2Stats, workoutDayToWrite, setNum, workout1, workout2, workout1Sets, workout2Sets):
        with open('Workouts.csv', 'a', newline='') as csvfile:
            WorkoutWriter = csv.writer(csvfile, delimiter=',')
            WorkoutWriter.writerow(["Day " + str(workoutDayToWrite) + " Workouts", time.strftime("%Y-%m-%d")])
            WorkoutWriter.writerow([workout1, workout1Sets, '', workout2, workout2Sets])
            for i in range(setNum):
                WorkoutWriter.writerow(['Set ' + str(i + 1), workout1Stats[i], '', 'Set ' + str(i + 1), workout2Stats[i]])
            WorkoutWriter.writerow('')
            WorkoutWriter.writerow('')
        if (workoutDayToWrite == 1):
            self.nextDay = 2
        elif (workoutDayToWrite == 2):
            self.nextDay = 3
        elif (workoutDayToWrite == 3):
            self.nextDay = 4
        elif (workoutDayToWrite == 4):
            self.nextDay = 1
        dayFile = open("DayFile.txt", "w")
        dayFile.write(str(self.nextDay))

