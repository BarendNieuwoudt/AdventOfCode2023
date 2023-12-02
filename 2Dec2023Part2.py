f = open("Data.txt", "r")
d = f.read().strip().split("\n") 
f.close()

max = {
	'red':12,
	'green':13,
	'blue':14
}

e = {}
sumOfPower = 0

for i in range(len(d)):
	currGame = int(d[i].split(': ')[0].split(' ')[1])
	e[currGame] = d[i].split(': ')[1].split('; ')
	
	power = {}
	
	for currSet in range(len(e[currGame])):
		s = e[currGame][currSet].split(', ')
		
		for currDraw in s:
			col = currDraw.split(' ')[1]
			count = int(currDraw.split(' ')[0])
			
			if col in power.keys():
				if power[col] < count:
					power[col] = count
			else:
				power[col] = count
	
	m = 1
	for n in power.keys():
		m = m * int(power[n])
	sumOfPower += m
	
print(sumOfPower)