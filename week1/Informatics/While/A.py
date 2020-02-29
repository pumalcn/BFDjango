import math
i = 1
n = int(input())

while(i <= n):
	if(int(math.sqrt(i)) ** 2 == int(i)):
		print(i)
	i += 1