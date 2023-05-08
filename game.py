import random

# Define the choices and their corresponding indexes
choices = ['A', 'B', 'C', 'D']
indexes = [0, 1, 2, 3]

# Generate two random choices and their indexes
choice1 = random.choice(choices)
index1 = indexes[choices.index(choice1)]

choice2 = random.choice(choices)
index2 = indexes[choices.index(choice2)]

# Print the choices and indexes
print(f"Choice 1: {choice1} ({index1})")
print(f"Choice 2: {choice2} ({index2})")



