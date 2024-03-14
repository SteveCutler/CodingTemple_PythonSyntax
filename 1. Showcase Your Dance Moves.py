# Task 1: Code Correction
# Below is a piece of Python code with incorrect indentation. Your task is to correct it.

# weather = "sunny"

# if weather == "sunny":
# print("Wear sunglasses!")
# else:
# print("Take an umbrella!")
weather = "sunny"
if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

print("\n")
# Task 2: Your Mood Today
# Ask the user how they feel today. 
# If they say "happy", print "That's great to hear!", 
# and if they say "sad", print "I hope your day gets better!". 
# Ensure your if statement is properly indented.

# By the end of this assignment, you should feel more confident 
# about how if statements work in Python and 
# how to indent them properly.

mood = input("How do you feel today? \n")
if mood == "sad":
    print("I hope your day gets better!")
elif mood == "happy": 
    print("That's great to hear!")
else: print("Please respond with either 'happy' or 'sad'. There are no other ways to feel!")