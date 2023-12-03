"""Made by: Mathias Herløv Lund 03/12/2023 
    Description:
    The water level of a river is measured (in meters) and recorded every hour. An alarm is triggered if any of the following
    two conditions are met:
    1. The water level has risen by more than 0.2 meters during the last hour, and the resulting water level is higher
    than 1.5 meters.
    2. The water level is above 2.0 meters.
    The water level measurements are stored in a list called water_levels. Your task is to write a function that returns
    the index of the first alarm. If no alarm is triggered, the function should return -1. All inequalities are strict (< is strict
    whereas ≤ is not); for example, a water level of exactly 2.0 meters is not enough to trigger an alarm.

    Input:  list called water_levels.
    
    Output: the index of the first alarm. If no alarm is triggered, the function should return -1.
"""
#Import the necessary libraries
import os  

#Find directory of python file
path=os.path.dirname(os.path.abspath(__file__))
#Change directory
os.chdir(path)

#os.chdir("C:/Users/mathi/Documents/GitHub/Examcafe_Introductory_Programming/Suggested_solutions")

def first_alarm(water_levels):
    #First we check if the water level is above 2.0 meters
    if max(water_levels) > 2.0:
        return water_levels.index(max(water_levels))
    #If the water level is not above 2.0 meters, we check if the water level has risen by more than 0.2 meters during the last hour, and the resulting water level is higher than 1.5 meters.
    else:
        for i in range(len(water_levels)-1):
            if water_levels[i+1] - water_levels[i] > 0.2 and water_levels[i+1] > 1.5:
                return i+1
        return -1

#Test the function
a = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
print(first_alarm(a))

#Another test
print(first_alarm([1.52, 1.29, 1.32, 1.18, 1.45, 1.63, 1.81, 1.95, 2.11, 2.09, 1.98, 1.3]))