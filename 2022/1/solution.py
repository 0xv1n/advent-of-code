import os

with open(os.path.dirname(__file__) + "/input.txt") as f:
    input = f.readlines()

calories = [0]

cals = 0
i = 0
for line in input:
    if line != "\n":
        cals += int(line)
    else:
        calories.insert(i, cals)
        cals = 0
        i = i + 1

# prints highest calorie count
print(max(calories))

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
print(sum(sorted(calories, reverse=True)[:3]))
