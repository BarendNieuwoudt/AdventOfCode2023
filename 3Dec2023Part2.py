f = open("Data.txt", "r")
d = f.read().strip().split("\n") 
f.close()

ratios = {}
finalRatios = {}

def updateratios():
	try:
		if gearCoords != "":
			if gearCoords in ratios.keys():
				finalRatios[gearCoords] = ratios[gearCoords] * int(numStr)
			else:
				ratios[gearCoords] = int(numStr)
	except:
		pass

for i in range(len(d)):
	line = d[i]
	
	numStr = ""
	gearCoords = ""
	
	for y in range(len(line)):
		char = line[y]
		if char.isnumeric():
			for r in [y-1, y, y+1]:
				for l in [i-1, i, i+1]:
					try:
						if not d[l][r].isnumeric() and d[l][r] == '*':
							gearCoords = f"{l}:{r}"
					except IndexError as e:
						pass
			numStr = numStr + char
		else:
			updateratios()
			gearCoords = ""
			numStr = ""
	updateratios()
	gearCoords = ""
	numStr = ""

sum = 0
for num in finalRatios.keys():
	sum += finalRatios[num]
print(sum)

# 77509019