'''
By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
'''
n1 = 1
n2 = 2
sum = 0
while n1 < 4000000:
	if n1 % 2 == 0:
		sum += n1
	n2 += n1
	n1 = n2-n1
print(sum)
