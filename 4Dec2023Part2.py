f = open("Data.txt", "r")
d = f.read().strip().split("\n") 
f.close()

cards = {}

for i in d:
	card = int(list(filter(None,i.split(':')[0].split(' ')))[1])
	winNums = list(filter(None, i.split(':')[1].strip().split(' |')[0].split(' ')))
	cardNums = list(filter(None, i.split(':')[1].strip().split('| ')[1].split(' ')))
	
	cards[card] = {'count': 1, 'wins':winNums, 'nums':cardNums}

for c in cards.keys():
	cardsToCopy = c + 1
	for n in cards[c]['nums']:
		if n in cards[c]['wins']:
			cards[cardsToCopy]['count'] += cards[c]['count']
			cardsToCopy += 1

totalCards = 0

for c in cards.keys():
	totalCards += cards[c]['count']

print(totalCards)

# 11787590
