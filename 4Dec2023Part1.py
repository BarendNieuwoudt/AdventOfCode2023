f = open("Data.txt", "r")
d = f.read().strip().split("\n") 
f.close()

totalPoints = 0

for i in d:
	card = int(list(filter(None,i.split(':')[0].split(' ')))[1])
	winNums = list(filter(None, i.split(':')[1].strip().split(' |')[0].split(' ')))
	cardNums = list(filter(None, i.split(':')[1].strip().split('| ')[1].split(' ')))
	
	points = 0
	for n in cardNums:
		if n in winNums:
			if points == 0: points = 1
			else: points = points*2
	totalPoints += points
			
print(totalPoints)

# 18519