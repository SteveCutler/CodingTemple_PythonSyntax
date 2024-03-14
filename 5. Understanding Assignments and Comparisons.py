# Objective:
# The aim of this assignment is to get a grasp on 
# how assignment operators work and how values can 
# be compared using comparison operators.

# Task 1: Value Swapping
# Swap the values of two given numbers using assignment 
# operators and then compare them to ensure they have been swapped.
x = 15
y = 100

if x > y:
    print("x =",x,"y =",y," therefore x is greater than y")
else:
    print("x =",x,"y =",y," therefore y is greater than x")

placeholder = x
x = y 
y = placeholder

if x > y:
    print("x =",x,"y =",y," therefore x is greater than y")
else:
    print("x =",x,"y =",y," therefore y is greater than x")

