#Advent of Code 2022, Day 1, Part 1 Solution

calories = [] 
calperelf = 0
with open('input1.txt') as f:
    for line in f:
        if line.strip():
            calperelf += int(line.strip())
        else:
            calories.append(calperelf)
            calperelf = 0
    print(max(calories))
        
