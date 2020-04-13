'''
Author: Derek Martin
Credit: CIS 122
Description: Create two functions to help calculate the amount of cement in yards, and display the results.
References: https://www.concretenetwork.com/concrete/howmuch/calculator.htm  https://www.todayshomeowner.com/cubic-yard-calculator/
'''

import math

# Calculate cement in yards using cubic inches given thickness in inches (t), width in inches (w) and length (l) in inches
def calc_yards_cement(t,w,l):
    cubic_inches = (t*w*l)
    yards = cubic_inches / (math.pow(36,3))
    return yards

# Output results of calculating yards given thickness in inches (t), width in inches (w) and length (l) in inches
def print_results(t,w,l):
    print("A cement slab", str(t) + "\" thick,", str(w) + "\" wide and", str(l) + "\" long requires", round((calc_yards_cement(t,w,l)),2), "yards of cement")

# Test
# print_results(4,120,240)
# print_results(4,360,360)
