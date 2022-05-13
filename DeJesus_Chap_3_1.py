#Date 09/11/2017
#Name Daniel De Jesus

#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
#hourly rate for hours worked above 40 hours.

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

if hrs > 40:
	overtime = hrs - 40
	regpay = 40 * rate
	overpay = (rate * 1.5) * overtime
	totalpay = (overpay + regpay)
	print("Pay: ", totalpay)
else : 
	regpay = hrs * rate
	print("Pay: ",regpay)
