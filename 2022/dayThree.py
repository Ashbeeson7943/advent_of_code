# split string in two/ compare for same char/ find weight of char/add up all weights

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
count = 1
bagCheck = []
bagChackGroup = []
for bag in data:
    if count > 3:
        bagCheck.append(bagChackGroup)
        bagChackGroup = []
        count = 1
    bagChackGroup.append(bag)
    firstpart, secondpart = bag[:len(bag)//2], bag[len(bag)//2:]
    sameChar = ''
    for fChar in firstpart:
        for sChar in secondpart:
            if fChar == sChar:
                 sameChar = fChar
    
    weight.append(getCharWeight(sameChar))
    count+=1

for w in weight:
    totalWeight += w


print(weight)
print(totalWeight)

print (bagCheck)