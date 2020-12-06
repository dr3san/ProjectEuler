n = 0
found = False
isnt = False
while not found:
	isnt = False
	n += 1
	for i in range(1,21):
		if n % i != 0:
			isnt = True
		if isnt:
			break
	if not isnt:
		found = True
print(n)
