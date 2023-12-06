f = open("Data.txt", "r")
data = f.read().strip().split("\n") 
f.close()

data = list(filter(lambda x: len(x) > 0, data))

t = data[0].split(": ")[1].split()
d = data[1].split(": ")[1].split()

c = 0
for x in range(len(t)):
	for ht in range(int(t[x])):
		dx = ht * (int(t[x]) - ht)
		if dx > int(d[x]):
			c += 1
print(c)