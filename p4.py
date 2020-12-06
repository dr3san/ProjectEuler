palindromes = []
for i in range(999, 99, -1):
	for j in range(999, 99, -1):
		product = str(i * j)
		part1 = product[0] + product[1] + product[2]
		part2 = product[-1] + product[-2] + product[-3]
		if part1 == part2:
			palindromes.append(int(product))

print(max(palindromes))
