'''
Author: Derek Martin
Credit: CIS 122
Description: Create two functions to help calculate the travel time in hours, minutes and seconds and to display the results.
References: https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php
'''

# Calculate travel time in hours, minutes and seconds given the distance in miles and the speed in mph
def calc_travel_time(distance,speed):
    hours = distance // speed
    mins = int(60 * ((distance / speed) - hours))
    seconds = int((((60 * ((distance / speed) - hours))) - mins) * 60)
    return print("To travel", distance, "miles at", speed, "MPH will take", hours, "hr,", mins, "min and", seconds, "sec")


# Output the travel time given distance and speed
def print_travel_time(distance,speed):
    return (calc_travel_time(distance,speed))

# Test
print_travel_time(110,60)
print_travel_time(110,70)
print_travel_time(5,25)
print_travel_time(5,45)
