#Date 09/01/2017
#Name Daniel De Jesus

#Exercise 3: Write a program to prompt the user for hours and rate per hour to
#compute gross pay.
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25

hrs = float(input("Enter hours: "))  #Prompts user for the hours worked as a float value.
rt = float(input("Enter Rate: "))    #Prompts user for the rate as a float value.
gross = str(hrs * rt)				 #Multiplys the hours by the rate as a string and assigns it to 'gross'.
print("Pay: " + gross)				 #Displays the Pay calling the value of gross.
