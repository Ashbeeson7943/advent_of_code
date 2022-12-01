import re

def split_on_empty_lines(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())


with open('2022/data/dayOneData.txt', 'r') as file:
    data = file.read()



individualData = split_on_empty_lines(data)

individualValues = []

for x in individualData:
    value = 0
    d = x.split('\n')
    for y in d:
        value += int(y)
    individualValues.append(value)
    
highestValue = 0
secondHighest = 0
thirdHighest = 0

for value in individualValues:
    if(value > highestValue):
        highestValue = value
    if(value > secondHighest) and (value < highestValue):
        secondHighest = value
    if(value > thirdHighest) and (value < secondHighest):
        thirdHighest = value
        
print ('First:' + str(highestValue))
print ('Second:' + str(secondHighest))
print ('Third:' + str(thirdHighest))
print ('Combined Three:' + str(highestValue + secondHighest + thirdHighest))