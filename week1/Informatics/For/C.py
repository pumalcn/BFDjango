import math
a = int(input())
b = int(input())

for i in range(a, b+1):
	if(int(math.sqrt(i)) ** 2 == int(i)):
		print(i, end = " ")