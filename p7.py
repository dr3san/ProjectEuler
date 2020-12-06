n = 10000000 #10 milli
primality = [True for i in range(n)]
print(len(primality))
primality.insert(0, False)
primes = []

for i, isprime in enumerate(primality):
	if isprime and i != 1:
		primes.append(i)
		for j in range(2*i,n+1,i):
			primality[j] = False
print(primes[0])
print(primes[1])
print(primes[2])
print(primes[3])
print(primes[10000])
