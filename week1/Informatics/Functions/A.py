def min_num(a, b, c, d):
	if a<=b and a<=c and a<=d:
		return a
	elif b<=a and b<=c and b<=d:
		return b
	elif c<=a and c<=b and c<=d:
		return c
	return d

a, b, c, d = list(map(int, input().split()))
print(min_num(a, b, c, d))