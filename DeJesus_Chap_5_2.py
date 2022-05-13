#Daniel De Jesus
#10/09/17

#Exercise 2: Write another program that prompts for a list of numbers as above
#and at the end prints out both the maximum and minimum of the numbers instead
#of the average.

Max = 0
Min = 0
Count = 0

def main():
	InputNum()

def InputNum():
	global Max
	global Min
	global Count
	Num = input("Enter a number: ")
	if (Num != 'done'):
		try:
			NumInt = int(Num)
			CheckMinMax(NumInt)
			InputNum()
		except ValueError:
			print("invalid input")
			InputNum()
	elif (Num == 'done'):
		print(Max, Min)

def CheckMinMax(Num):
	global Max
	global Min
	global Count
	if (Num > Max):
		Max = Num
		if Count is 0:
			Count += 1
			Min = Num
		InputNum()
	elif (Num < Min):
		Min = Num
		InputNum()
		
main()
	
