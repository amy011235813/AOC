#Advent of Code 2022, Day 1, Part 2 Solution

calories = [] 
calperelf = 0
topthree = 0
with open('input1.txt') as f:
    for line in f:
        if line.strip():
            calperelf += int(line.strip())
        else:
            calories.append(calperelf)
            calperelf = 0
    #print(max(calories))
    calories.sort(reverse=True)
    topthree = calories[0] + calories[1] + calories[2]
    print(topthree)
