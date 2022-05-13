#Daniel De Jesus
#09/28/17

#Exercise 7: Rewrite the grade program from the previous chapter using a function
#called computegrade that takes a score as its parameter and returns a grade as a
#string.
#Score Grade
#> 0.9 A
#> 0.8 B
#> 0.7 C
#> 0.6 D
#<= 0.6 F

test_score1 = 0

def score_check(x):
	print("the score you have entered is not valid. Please try again")
	y = x
	computegrade(y);
	
def computegrade(x):
	if (x == 0 or x == 1):
		test1 = input("Please enter the first test score (0.0 - 1.0):")
		try:
			global test_score1;
			test_score1 = float(test1)
			if test_score1 <= 1.0:
				x = 2
				computegrade(x);
			else:
				x = 1
				score_check(x);
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
		
computegrade(0);
