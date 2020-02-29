question1 = int(input('What did you get for the Assignment 1? ')) #asking about score for the Assignment1
print('')
question2 = int(input('What did you get for the Assignment 2? ')) #asking about score for the Assignment2
print('')
question3 = int(input('What did you get for the Assignment 3? ')) #asking about score for the Assignment3
print('')
question4 = int(input('What are you expecting get for the Midterm Exam? ')) #asking about expected grade for the Midterm
print('')
score = question1 + question2 + question3 + question4 # calculates score of 3 assignments & midterm
perScore = (score * 100)/45 #calculates percentage score based on score
#following function returns your grade according to score
def final(overall):
	if overall <= 45 and overall >= 42.75:
		return 'A+'
	elif overall < 42.75 and overall >= 40.5:
		return 'A0'
	elif overall < 40.5 and overall >= 38.25:
		return 'B+'
	elif overall < 38.25 and overall >= 36:
		return 'B0'
	elif overall < 36 and overall >= 33.75:
		return 'C+'
	elif overall < 40.5 and overall >= 31.5:
		return 'C0'
	elif overall < 31.5 and overall >= 29.25:
		return 'D+'
	elif overall < 29.25 and overall >= 27:
		return 'D0'
	elif overall < 27:
		return 'F'

print('Raw Score: ' + str(score)) #printing Raw Score
print('')
print('% Score: ' + str(perScore)) #printing Percentage Score
print('')
print('Letter Grade: ', final(score)) #printing Letter Grade
print('')