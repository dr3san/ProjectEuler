n = 600851475143

def isPrime(n):
	if n == 1:
		return False
	else:
		for i in range(2, n):
			if n % i == 0:
				return False
	return True

oldfactor = 0
newfactor = 1
while oldfactor != newfactor:
	oldfactor = newfactor
	for i in range(2, n):
		if isPrime(i) and n % i == 0:
			newfactor = i
			n = n // newfactor
			break
print(n)
