# Objective:
# The aim of this assignment is to grasp the concept 
# of logical operations and understand how operator 
# precedence can affect the outcome of an operation.

# Task 1: Validating Calculations
# Calculate the value of a particular arithmetic 
# expression twice: once normally, and once using parentheses. 
# Compare the two results to see if they match.
value = 10 + 100 / 17 * 654 ** 2
print ("the first value = ", value)
value2 = (10 + (100 / 17)) * 654 ** 2
print("the second value = ",value2)

print("The two values are equal to each other: ",value == value2)

print("\n")

# Task 2: Mix and Match
# Combine arithmetic, logical, and comparison operators 
# in a single expression and predict the outcome. 
# Then, compute the expression to see if the prediction was correct.


expression = 10 * 100 and 999 + 1 == 1000
print("if the expression is: 10 * 100 and 999 + 1 == 1000")
print("the outcome will be True") 
print("the outcome of the expression is", expression)
