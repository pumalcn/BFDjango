def xor(a, b):
	if a == b:
		return 0
	else:
		return 1

a, b = [int(x) for x in input().split()]
print(xor(a, b))