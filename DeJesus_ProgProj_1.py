#Daniel De Jesus
#09/20/17

#James wants to buy a motorcycle. Help James compute the monthly payment on a loan, given the loan amount, 
#the annual percentage rate of interest, and the number of monthly payments. 
#The program should allow James to input the loan amount, interest rate, and how many payments he wants to make. 
#It should then compute and display the monthly payment.

Payment = 0																				#Lines 9 to 13 are setting the following as global variables: Payment, LoanAmt, InterestRate, MonthlyRate, NumberMonths.
LoanAmt = 0
InterestRate = 0
MonthlyRate = 0
NumberMonths = 0

def Interest_input(x):																	#Defines Interest_Input as a function with a parameter of x
	if (x == 0):																		#Creates an If-Else statment that checks if x is logically equal to 0
		loan = input("Please enter the loan amount: ")									#Requests input and set the value as loan
		try:																			#try will try to complete lines 19 to 22
			global LoanAmt;																#Calls the global variable LoanAmt
			LoanAmt = round(float(loan),3)												#Coverts and round the loan input to a float to 2 decimals and assigns to LoanAmt
			x = 1																		#Assigns x with the value of 1
			Interest_input(x);															#Calls the function Interest_Rate and passes the value of x
		except ValueError:																#If try has a value error it will run lines 24 to 25
			x = 0																		#Assigns x the value of 0
			check_error(x);																#Calls the function check_error and passes the x value
	elif (x == 1):																		#Continues the If statment in line 17 and checks if x is logically equal to 1
		IntRate = input("Please enter the annual interest rate(%): ")					#Requests input and sets the value as IntRate
		try:																			#try will try to complete lines 29 to 32
			global InterestRate;														#Calls the global variable InterestRate
			InterestRate = round(float(IntRate),3)										#Converts and round the IntRate to a float to 3 decimals and assigns to InterestRate
			x = 2																		#Assigns x the value of 2
			Interest_input(x);															#Calls the function Interest_input and passes the value of x
		except ValueError:																#If try has a value error it will run lines 34 to 35
			x = 1																		#Assigns x the value of 1
			check_error(x);																#Calls the function check_error and passes the value of x
	elif (x == 2):																		#Continues the If statment in line 17 and checks if x is logically equal to 2
		NumMo = input("Please enter the number of monthly payments(months): ")			#Requests input and set the value as NumMo
		try:																			#try will try to complete lines 39 to 42
			global NumberMonths;														#Calls the global variable NumberMonths
			NumberMonths = int(NumMo)													#Coverts to an integer and assigns to NumberMonths
			x = 3																		#Assigns x the value of 3
			Interest_input(x);															#Calls the function Interest_input and passes the value of x
		except ValueError:																#If try has a value error it will run lines 44 to 45
			x = 2																		#Assigns x the value of 2
			check_error(x);																#Calls the function check_error and passes the value of x
	else:																				#Else that completes the If statment in line 17
		pay_MoRate();																	#Calls the function pay_MoRate
		
def check_error(x):																		#Defines the function check_error
	print("you have entered and incorrect value please try again.")						#Displays that the last input was not able to be converted
	y = x																				#Assigns y the value of x
	Interest_input(y);																	#Calls the function Interest_input and passes the value of y
	
def pay_MoRate():																		#Defines the function pay_MoRate
	global Payment;																		#Lines 55 to 59 call the global variables Payment,LoanAmt,InterestRate,MonthlyRate,NumberMonths
	global LoanAmt;																		
	global InterestRate;																
	global MonthlyRate;																	
	global NumberMonths;																
	MonthlyRate = round(float((InterestRate / (100 * 12))),6)					#Converts and rounds the calculation to 6 decimals and assigns to MonthlyRate
	Payment = round(float(LoanAmt * MonthlyRate * (((1 + MonthlyRate)**NumberMonths)/(((1 + MonthlyRate)**NumberMonths) - 1))),2) #Converts and rounds the calculation to 2 decimals and assigns to Payment
	print("The Payment is: ", Payment, " and the monthly rate is: ", MonthlyRate)		#Displays the payment and monthly rate

Interest_input(0);																		#Calls the function Interest_input and passes the value of 0
