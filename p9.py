triplets = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
(20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53),
(11, 60, 61), (16, 63, 65), (33, 56, 65), (48, 55, 73),
(13, 84, 85), (36, 77, 85), (39, 80, 89), (65, 72, 97)]

for triplet in triplets:
	print(1000 / sum(triplet))

result = (25*8, 25*15, 25*17)
print(sum(result))

answer = 1

for side in result:
	answer *= side

print(answer)