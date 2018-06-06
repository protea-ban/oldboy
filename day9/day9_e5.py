sum_num = 0
n = 1
while n <= 99:
	if n % 2 == 1:
		sum_num += n
	elif n % 2 == 0:
		sum_num -= n
	n += 1
print(sum_num)