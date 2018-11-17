import math
num=int(input())

for i in range(0, math.sqrt(num)):
	if num % i == 0:
		print('not prime')
else:
	print('prime')
