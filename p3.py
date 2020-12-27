'''
What is the largest prime factor of the number 600851475143 ?
'''

n = 600851475143

def isPrime(n):
	if n == 1:
		return False
	else:
		for i in range(2, n):
			if n % i == 0:
				return False
	return True

while n != 1:
	for i in range(2, n+1):
		if isPrime(i) and n % i == 0:
			factor = i
			n = n // factor
			break
print(factor)
