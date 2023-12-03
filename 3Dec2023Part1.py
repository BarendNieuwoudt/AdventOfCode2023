f = open("Data.txt", "r")
d = f.read().strip().split("\n") 
f.close()

partNums = []

def updatePartNums(bordersOn):
	try:
		if bordersOn:
			partNums.append(int(numStr))
			bordersOn = False
	except:
		pass
	return bordersOn

for i in range(len(d)):
	line = d[i]
	numStr = ""
	bordersOn = False
	for y in range(len(line)):
		char = line[y]
		if char.isnumeric():
			for r in [y-1, y, y+1]:
				for l in [i-1, i, i+1]:
					try:
						if not d[l][r].isnumeric() and d[l][r] != '.':
							bordersOn = True
					except IndexError as e:
						pass
			numStr = numStr + char
		else:
			bordersOn = updatePartNums(bordersOn)
			numStr = ""
	bordersOn = updatePartNums(bordersOn)
	numStr = ""
	
sum = 0
for num in partNums:
	sum += num
print(sum)

# 529618