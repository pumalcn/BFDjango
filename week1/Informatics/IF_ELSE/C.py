program = int(input())
pupil = int(input())

if(program != 1 and pupil != 1):
	print("YES")
elif(program == 1 and pupil == 1):
	print("YES")
elif(program == 1 and pupil != 1):
	print("NO")
elif(program != 1 and pupil == 1):
	print("NO")
