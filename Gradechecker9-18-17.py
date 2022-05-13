# Daniel De Jesus
# 09-18-2017

#This program will accept three test scores find the average and the 
#display a corresnding grade.
test_score1 = 0
test_score2 = 0
test_score3 = 0

def score_check(x):
	print("the score you have entered is not valid. Please try again")
	y = x
	get_score(y);
	
def get_score(x):
	if (x == 0 or x == 1):
		test1 = input("Please enter the first test score (0-100):")
		try:
			global test_score1;
			test_score1 = float(test1)
			if test_score1 > 101:
				x = 1
				score_check(x);
			x = 2
			get_score(x);
		except ValueError:
			x = 1
			score_check(x);	
	if (x == 2):
		test2 = input("Please enter the second test score (0-100):")
		try:
			global test_score2;
			test_score2 = float(test2)
			if test_score2 > 101:
				x = 2
				score_check(x);
			x = 3
			get_score(x);
		except ValueError:
			x = 2
			score_check(x);
	if (x == 3):
		test3 = input("Please enter the third test score (0-100):")
		try:
			global test_score3;
			test_score3 = float(test3)
			if test_score3 > 101:
				x = 3
				score_check(x);
			x = 4
			get_score(x);		
		except ValueError:
			x = 3
			score_check(x);
	if x > 3:
		testAvg = float((test_score1 + test_score2 + test_score3)/3)
		print("---------------------------------------------------")
		print("The average of the test scores is :" + str(testAvg))
		exit();
		
get_score(0);
