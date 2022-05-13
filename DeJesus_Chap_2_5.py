#Date 09/01/2017
#Name Daniel De Jesus

#Exercise 5: Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the converted temperature.

print("This program will convert the temperature from Celsius to Fahrenheit.") #Informs user the purpose of the program.
C = float(input("Please enter the temperature in Celsius: "))				   #Accepts the input from the user as a floating value in Celsius.
F = str(C * 1.8 + 32)														   #Multiplys the input value by 1.8 and adds 32 and converts to a string.
print("The temperature in Fahrenheit is: " + F)								   #Displays the converted value.
