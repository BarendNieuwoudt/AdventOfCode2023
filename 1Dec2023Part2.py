n = {
  'zero': '0',
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

f = open("1Dec2023Data.txt", "r")
i = f.read().strip().split("\n") 
f.close()

s = 0

for l in i:
	d = []
	for c in range(len(l)):
		if l[c].isnumeric():
			d.append(l[c])
		else:
			for e in n.keys():
				if l[c:].startswith(e):
					d.append(n[e])
					continue
	s += int(d[0] + d[len(d)-1])

print(s)

#Expecting: 55701
