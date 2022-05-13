#Daniel De Jesus
#10/2/2017

#A finance company provides loans for motorcycles at different rates 
#depending on how much the total loan amount is and how many payments 
#will be made on the loan. Using the information in the table below, 
#write a program that will calculate the monthly payment based on user 
#inputs of loan amount and number of monthly payments. The user will NOT 
#input the percentage rate, as this will be determined by the program code 
#based on user input of loan amount and number of payments. The output will 
#display the loan amount, number of payments, monthly payments and the 
#interest rate of the loan. Use a loop to allow users to enter as many sets
# of data as desired. At the end of each loop, ask the user if he or she 
#would like to Exit the program (Y for Yes or N for No). If yes, clear 
#the variables and repeat the input, processing and output loop. 
#If no, exit the program.

def InputLoan(x, Loan, NumPay):											#defines the function InputLoan with three parameters x, Loan, NumPay
	if x == 0:															#beginning if statement, if x is logially equal to zero
		Loan = input("Please enter the desired loan amount: $")			#Variable Loan set to accept input 
		check_num(1, Loan, 0)											#Calls for the function check_num passing along three variables
	elif x == 1:														#else-if statment continuing the original if statment checking if x is logically equal to 1
		NumPay = input("Please enter the desired number of payments(between 6 and 48) : ")#Variable NumPay set to accept input
		check_num(2, Loan, NumPay)										#Calls for the function check_num passing along three variables
	else:																#else statment to close the original if statement
		RateBracket(Loan, NumPay)										#Calls for the function RateBracket passing two variables
			
def RateBracket(Loan, NumPay):											#defines the function RateBracket with two parameters Loan and NumPay
	if (Loan >=	500 and Loan <= 2500):									#Beginning if statement, if Loan is greater than or equal to 500 and Loan is less than or equal to 2500
		Interest1(Loan, NumPay)											#calls for the function Interest1 passing two variables
	elif (Loan >= 2501 and Loan <= 10000):								#else-if statement, if Loan is greater than or equal to 2501 and loan is less than or equal to 10000
		Interest2(Loan, NumPay)											#calls for the function Interest2 passing two variables
	else:																#else ending the original if statment
		Interest3(Loan, NumPay)											#calls for the function Interest3 passing two variables

def Interest1(Loan , NumPay):											#defines Interest1 with two parameters Loan and NumPay
	if (NumPay >= 6 and NumPay <= 12):									#beginning if statement, if NumPay is greater than or equal to 6 and NumPay is less than or equal to 12
		IntRate = 8														#assigns IntRate the value of 8
		Months = NumPay													#assigns Months to the value stored in variable NumPay
		calculations(Loan, NumPay, IntRate, Months)						#calls for the function calculations passing four variables
	elif (NumPay >= 13 and NumPay <= 36):								#else-if statement, if NumPay is greater than or equal to 13 and NumPay is less than or equal 36
		IntRate = 10													#assigns IntRate the value 10
		Months = NumPay													#assigns Months tha value stored in NumPay
		calculations(Loan, NumPay, IntRate, Months)						#calls for the function calculations passing four variables
	elif (NumPay >= 37 and NumPay <= 48):								#else-if statement, if NumPay is greater than or equal to 37 and NumPay is less than or equal 48
		IntRate = 12													#assigns IntRate the value 12
		Months = NumPay													#assigns Months tha value stored in NumPay
		calculations(Loan, NumPay, IntRate, Months)						#calls for the function calculations passing four variables
	else:																#else ending the beginning if statement 
		print("The number of payments must be between 6 and 48, please try again.")#outputs error in amount of payments desired
		InputLoan(1, Loan, NumPay)										#calls for the function InputLoan passing three variables
			
def Interest2(Loan , NumPay):											#defines Interest2 with two parameters Loan and NumPay
	if (NumPay >= 6 and NumPay <= 12):									#beginning if statement, if NumPay is greater than or equal to 6 and NumPay is less than or equal to 12
		IntRate = 7														#assigns IntRate the value of 7
		Months = NumPay													#assigns Months to the value stored in variable NumPay
		calculations(Loan, NumPay, IntRate, Months)						#calls for the function calculations passing four variables
	elif (NumPay >= 13 and NumPay <= 36):								#else-if statement, if NumPay is greater than or equal to 13 and NumPay is less than or equal 36
		IntRate = 8														#assigns IntRate the value 8
		Months = NumPay													#assigns Months tha value stored in NumPay
		calculations(Loan, NumPay, IntRate, Months)						#calls for the function calculations passing four variables
	elif (NumPay >= 37 and NumPay <= 48):								#else-if statement, if NumPay is greater than or equal to 37 and NumPay is less than or equal 48
		IntRate = 6														#assigns IntRate the value 6
		Months = NumPay													#assigns Months tha value stored in NumPay
		calculations(Loan, NumPay, IntRate, Months)						#calls for the function calculations passing four variables
	else:																#else ending the beginning if statement 
		print("The number of payments must be between 6 and 48, please try again.")#outputs error in amount of payments desired
		InputLoan(1, Loan, NumPay)										#calls for the function InputLoan passing three variables
		
def Interest3(Loan , NumPay):											#defines Interest3 with two parameters Loan and NumPay
	if (NumPay >= 6 and NumPay <= 12):									#beginning if statement, if NumPay is greater than or equal to 6 and NumPay is less than or equal to 12
		IntRate = 5														#assigns IntRate the value of 5
		Months = NumPay													#assigns Months tha value stored in NumPay
		calculations(Loan, NumPay, IntRate, Months)						#calls for the function calculations passing four variables
	elif (NumPay >= 13 and NumPay <= 36):								#else-if statement, if NumPay is greater than or equal to 13 and NumPay is less than or equal 36
		IntRate = 6														#assigns IntRate the value of 6
		Months = NumPay													#assigns Months tha value stored in NumPay
		calculations(Loan, NumPay, IntRate, Months)						#calls for the function calculations passing four variables
	elif (NumPay >= 37 and NumPay <= 48):								#else-if statement, if NumPay is greater than or equal to 37 and NumPay is less than or equal 48
		IntRate = 7														#assigns IntRate the value of 7
		Months = NumPay													#assigns Months tha value stored in NumPay
		calculations(Loan, NumPay, IntRate, Months)						#calls for the function calculations passing four variables
	else:																#else ending the beginning if statement 
		print("The number of payments must be between 6 and 48, please try again.")#outputs error in amount of payments desired
		InputLoan(1, Loan, NumPay)										#calls for the function InputLoan passing three variables
		
def calculations(Loan, NumPay, IntRate, Months):						#defines the function calculations with four parameters Loan, NumPay, IntRate, and Months
	MonthlyRate = round(float(IntRate / (12 * 100)),6)					#assigns MonthlyRate the rounded and floated value of IntRate divided by 1200 to the sixth decimal
	MonthlyPayment = round(float(Loan * MonthlyRate * (((1 + MonthlyRate)**Months)/(((1 + MonthlyRate)**Months) - 1))),2)#calculates the monthly payment
	print("The loan amount is ", Loan, ", the number of payments: ", NumPay, ", monthly rate: ", MonthlyPayment, ", and the interest rate is: ", MonthlyRate,".")#outputs the loan, NumPay, and monthly payment
	menu()																#calls the function menu with no variables
	
def check_num(x, y, z):													#defines the function check_num with three parameters x, y, and z
	if x == 1:															#beginning if statement, if x is logically equal to 1
		try:															#try statement
			rounded = round(float(y),2)									#assigns the variable rounded the value of y floated and rounded to two decimals
			if rounded >= 500:											#nested if statement, if rounded is greater than or equal to 500
				InputLoan(1, rounded, 0)								#call the function InputLoan passing three variables
			else:														#else ending the nested if statement
				print("Sorry, We do not finance loans below $500.")		#output sorry no less then 500 loan
				menu()													#calls the function menu
		except ValueError:												#except ending if the try statment has a Value Error 
			print("The value entered was invalid please try again.")	#output invalid input error
			InputLoan(0, 0, 0)											#calls the function InputLoan passing three values that clear the previous user input
	else:																#else ending the beginning if statement
		try:															#try statement
			Int = int(z)												#assigns Int the value of z converted to an integer
			InputLoan(2, y, Int)										#calls the function InputLoan passing along three variables
		except ValueError:												#except statement if the try statement has a value error
			print("The value entered was invalid please try again.")	#output invalid input error
			InputLoan(1, y, 0)											#calls the function InputLoan passing along three values
		
def menu():																#defines the function menu
	print("If you would like to try again enter the letter Y.")			#outputs if the user wants to continue press y
	print("If you would like to exit enter the letter N.")				#outputs if the user wants to exit press n
	uservalue = input("Please enter Y or N: ")							#assigns uservalue the input of either y or n
	if (uservalue == 'Y' or uservalue == 'y'):							#beginning if statement, if user value is logically equal to 'Y' or is logically equal to 'y'
			import os													#imports operating system functions 
			os.system('cls')											#calls the operating system to clear the screen, (Mac OSX or Linux this command would be 'clear' instead of 'cls')
			InputLoan(0, 0, 0)											#calls the function InputLoan and clears all three variables
	elif (uservalue == 'N' or uservalue == 'n'):						#else-if statement, if uservalue is logically equal to 'N' or is logically equal to 'n'
			exit														#exits program
	else:																#else ending beginning if statement
		import os														#import operating system functions 
		os.system('cls')												#calls the operating system to clear the screen, (Mac OSX or Linux this command would be 'clear' instead of 'cls')
		print("The value you entered is not valid.")					#prints invalid input error
		menu()															#calls the function menu
def main():																#defines the function main
	InputLoan(0, 0, 0)													#calls the function InputLoan

main()																	#calls the function main, beginning the program.
