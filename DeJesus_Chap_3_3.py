#Date 09/13/2017
#Name Daniel De Jesus
#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
#score is out of range, print an error message. If the score is between 0.0 and 1.0,
#print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#~~~

test_score1 = 0

def score_check(x):
	print("the score you have entered is not valid. Please try again")
	y = x
	get_score(y);
	
def get_score(x):
	if (x == 0 or x == 1):
		test1 = input("Please enter the first test score (0.0 - 1.0):")
		try:
			global test_score1;
			test_score1 = float(test1)
			if test_score1 > 1.0:
				x = 1
				score_check(x);
			x = 2
			get_score(x);
		except ValueError:
			x = 1
			score_check(x);	
	else:
		Grade = round(float((test_score1)),2)
		print("---------------------------------------------------");
		if (Grade >= .9):
			print("A")
		elif (Grade >= .8):
			print("B")
		elif (Grade >= .7):
			print("C")
		elif (Grade >= .6):
			print("D")
		else:
			print("F")
			exit();
		
get_score(0);
