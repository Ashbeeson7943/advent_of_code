# rock = 1, paper = 2, scissors = 3
# 6 for win, 3 for draw, 0 for lost
# opp: A = rock, B = Paper, C = Scissors : Left Column
# you: X = rock, Y = paper, Z = Scissors : right column PART 1
# you: X = lose, Y = draw, Z - win : rigth colum PART 2


def calculateScore(game):
    values = game.split(' ')
    if values[0].upper() == 'A':
        if values[1].upper() == 'X':
            return 4
        elif values[1].upper() == 'Y':
            return 8
        elif values[1].upper() == 'Z':
            return 3
    elif values[0].upper() == 'B':
        if values[1].upper() == 'X':
            return 1
        elif values[1].upper() == 'Y':
            return 5
        elif values[1].upper() == 'Z':
            return 9
    elif values[0].upper() == 'C':
        if values[1].upper() == 'X':
            return 7
        elif values[1].upper() == 'Y':
            return 2
        elif values[1].upper() == 'Z':
            return 6

def calculateShapeAndScore(game):
    values = game.split(' ')
    if values[0].upper() == 'A':
        if values[1].upper() == 'X':
            return 3
        elif values[1].upper() == 'Y':
            return 4
        elif values[1].upper() == 'Z':
            return 8
    elif values[0].upper() == 'B':
        if values[1].upper() == 'X':
            return 1
        elif values[1].upper() == 'Y':
            return 5
        elif values[1].upper() == 'Z':
            return 9
    elif values[0].upper() == 'C':
        if values[1].upper() == 'X':
            return 2
        elif values[1].upper() == 'Y':
            return 6
        elif values[1].upper() == 'Z':
            return 7

data = []

with open('2022/data/dayTwoData.txt', 'r') as file:
    for line in file:
        data.append(line.rstrip())

partOneTotal = 0
partTwoTotal = 0

for game in data:
    partOneTotal += calculateScore(game)
    partTwoTotal += calculateShapeAndScore(game)
    
print ('Part 1:' + str(partOneTotal))
print ('Part 2:' + str(partTwoTotal))

