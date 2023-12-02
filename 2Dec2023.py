f = open("Data.txt", "r")
d = f.read().strip().split("\n") 
f.close()

max = {
	'red':12,
	'green':13,
	'blue':14
}

e = {}
sumPossibleGames = 0

for i in range(len(d)):
	currGame = int(d[i].split(': ')[0].split(' ')[1])
	e[currGame] = d[i].split(': ')[1].split('; ')
	
	currGamePossible = True
	
	for currSet in range(len(e[currGame])):
		s = e[currGame][currSet].split(', ')
		
		for currDraw in s:
			col = currDraw.split(' ')[1]
			count = int(currDraw.split(' ')[0])
			
			if max[col] < count:
				currGamePossible = False
				break;
		if currGamePossible == False:
			break;
			
	if currGamePossible:
		sumPossibleGames += currGame
	
print(sumPossibleGames)