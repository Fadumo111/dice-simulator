import random
from collections import Counter

def roll_die():
    random_number = random.uniform(0, 1)
    if random_number < 1/6:
        return 1
    elif random_number < 2/6:
        return 2
    elif random_number < 3/6:
        return 3
    elif random_number < 4/6:
        return 4
    elif random_number < 5/6:
        return 5
    else:
        return 6

# Run the simulation 1000 times
rolls = [roll_die() for _ in range(1000)]

# Count the frequency of each face
counter = Counter(rolls)

# Calculate the percentage for each face
total_rolls = len(rolls)
percentage = {face: round(count/total_rolls*100, 1) for face, count in counter.items()}

# Print the results
for face in range(1, 7):
    print(f"Face {face}: Frequency = {counter[face]}, Percentage = {percentage[face]}%")
