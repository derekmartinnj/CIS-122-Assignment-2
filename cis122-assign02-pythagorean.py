'''
Author: Derek Martin
Credit: CIS 122
Description:  Create two functions to calculate a missing side using the Pythagorean Theorem.
References: https://ncalculators.com/number-conversion/pythagoras-theorem.htm  http://mathforum.org/dr.math/faq/faq.pythagorean.html  https://docs.python.org/3/library/math.html
'''

# Question 1
import math

# Calculate missing side c
def calc_side_c(a,b):
    return(round(math.sqrt((math.pow(a,2))+(math.pow(b,2))),2))
      
# Calculate missing side a or b
def calc_side_ab(ab,c):
    return(round((math.sqrt((math.pow(c,2)) - (math.pow(ab,2)))),2))

# Test
# print("c =",calc_side_c(10,20))
# print("a =",calc_side_ab(4,5))
