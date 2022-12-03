#Advent of Code 2022, Day 2, Part 1 Solution

def input_to_number(input)
    if input = 'A' or 'X'
       return 1

elfchoice = ""
yourchoice = ""

with open('input2.txt') as f:
    for line in f:
        elfchoice = line[0]
        yourchoice = line[2]

        print(elfchoice," ",yourchoice)
        
