# Part 1: split string in two/ compare for same char/ find weight of char/add up all weights
# Part 2: each group of three contain the same char, find and point. then add together

def stringCompare(string1, string2):
    my_str = ''
    for w in set(string1):
        if w in string2:
            my_str += w
    return my_str

def getCharWeight(char):
    
    points = 1
    lp = 0
    up = 0
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    
    if char.isupper() :
        up = upper.index(char)
        points += up + 26
    else:
        lp = lower.index(char)
        points += lp 
        
    return points
  

data = []

with open('2022/data/dayThreeData.txt', 'r') as file:
    for line in file:
        data.append(line.rstrip())
    
totalWeight = 0
weight = []
count = 0
bagCheck = []
bagChackGroup = []
for bag in data:
    bagChackGroup.append(bag)
    firstpart, secondpart = bag[:len(bag)//2], bag[len(bag)//2:]
    sameChar = stringCompare(firstpart, secondpart)
    weight.append(getCharWeight(sameChar))
    count += 1
    if(count == 3):
        bagCheck.append(bagChackGroup)
        bagChackGroup = []
        count = 0

for w in weight:
    totalWeight += w


print('Part 1: ' + str(weight))
print('Part 1:' + str(totalWeight))

badgeWeight = 0
badgeSymbol = []

for bagGroup in bagCheck:
    # compare 1>2, comp 2>3, comp 1>3
    g1 = stringCompare(bagGroup[0], bagGroup[1])
    g2 = stringCompare(bagGroup[1], bagGroup[2])
    g3 = stringCompare(bagGroup[0], bagGroup[2])
    
    b1 = stringCompare(g1,g2)
    b2 = stringCompare(g2,g3)
    b3 = stringCompare(g1,g3)
    
    if b1 == b2 and b2 == b3:
        badgeSymbol.append(b1)

for badge in badgeSymbol:
    badgeWeight += getCharWeight(badge)
    
print('Part 2: ' + str(badgeSymbol))
print('Part 2: ' + str(badgeWeight))