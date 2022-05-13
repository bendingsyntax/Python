#Date 09/11/2017
#Name Daniel De Jesus

#Exercise 2: Rewrite your pay program using try and except so that your pro-
#gram handles non-numeric input gracefully by printing a message and exiting the
#program. The following shows two executions of the program
def Gross_Pay():
	try:
		hrs = float(input("Enter Hours:"))
		rate = float(input("Enter Rate:"))
		if hrs > 40:
			overtime = float(hrs - 40)
			regpay = float(40 * rate)
			overpay = float((rate * 1.5) * overtime)
			totalpay = float((overpay + regpay))
			print("Pay: ", round(totalpay,2))
		else : 
			regpay = hrs * rate
			print("Pay: ",regpay)
	except ValueError:
		print("You have entered an incorrect value please try again")
		Gross_Pay();
Gross_Pay();
