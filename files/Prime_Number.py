import math
num=int(input())

try:
	for i in range(1, int(math.sqrt(num))):
		if num % i == 0:
			print('not prime')
			break
	else:
		print('prime')
except:
	print('some error')



