#Daniel De Jesus
#10/09/17

#Exercise 1: Write a program which repeatedly reads numbers until the user enters
#“done”. Once “done” is entered, print out the total, count, and average of the
#numbers. If the user enters anything other than a number, detect their mistake
#using try and except and print an error message and skip to the next number.
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333
count = 0
total = 0

def main():
	EnterNum()

def EnterNum():
	Num = input("Enter a number: ")
	if (Num != 'done'):
		try:
			global count
			global total
			NumInt = int(Num)
			count += 1
			total += NumInt
			EnterNum()
		except ValueError:
			print("Invalid input")
			EnterNum()
	elif (Num == 'done' or Num == 'Done'):
		if (count > 0):
			avg = total / count
			print(total, count, avg)
		else:
			print(0, 0, 0)

main()
