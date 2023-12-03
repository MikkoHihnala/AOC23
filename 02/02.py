from pprint import pprint
inputData = open("../02/testinput", "r")
data  = inputData.readlines()

sum = 0 
games = []
#parse data with split() into game-> sets -> pulls

#define function to find if current pull exceeds the max values

def checkForMax(color, number): #return True if max pull is possible
    maxValues = {
            "red": 12,
            "green": 13,
            "blue": 14
            }
    for k,v in maxValues.items():
        if k == color and int(number)<=v: #this could be a oneliner?
            return True
    return False
 
#parse and split data
#remove the Game x -header from lines
for game in data:
    games.append(game.strip().split(": ")[1])

#split games in to sets
for line in range(len(games)):
    set = games[line]
    set = set.replace(";", ",") #the ; is useless for for now
    set = set.split(", ")
    games[line] = set
#split sets in to pulls
    for item in range(len(set)):
        pull = set[item].split(" ")
#check if pull is possible and set "set" as True if it is 
        if checkForMax(pull[1], int(pull[0])): # 1 = color, 0 is number
            games[line][item] = True 
        else:
            games[line][item] = False 
#if game is possible, add its indexvalue+1 to sum pool
for index in range(len(games)):
    if False not in games[index]:
        sum += index+1
print(sum)

