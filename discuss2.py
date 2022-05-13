import random;
import math;

var1=0
var2=0
var3=0
var4=0
var5=0
var6=0

def input_function(x):
	if x is 0:
		global var1
		val1 = input("Please enter the first random number ")
		try:
			var1 = float(val1)
			input_function(1)
		except ValueError:
			var1 = round(float(random.random()*100),2)
			input_function(1)
	elif x is 1:
		global var2
		val2 = input("Please enter the second random number ")
		try:
			var2 = float(val2)
			input_function(2)
		except ValueError:
			var2 = round(float(random.random()*100),2)
			input_function(2)
	elif x == 2:
		global var3
		val3 = input("Please enter the third random number ")
		try:
			var3 = float(val3)
			input_function(3)
		except ValueError:
			var3 = round(float(random.random()*100),2)
			input_function(3)
	elif x == 3:
		global var4
		val4 = input("Please enter the fourth random number ")
		try:
			var4 = float(val4)
			input_function(4)
		except ValueError:
			var4 = round(float(random.random()*100),2)
			input_function(4)
	elif x is 4:
		global var5
		val5 = input("Please enter the fifth random number ")
		try:
			var5 = float(val5)
			input_function(True)
		except ValueError:
			var5 = round(float(random.random()*100),2)
			input_function(True)
	elif x is True:
		global var6;
		val6 = input("Please enter the sixth random number ")
		try:
			var6 = float(val6)
			input_function(6)
		except ValueError:
			var6 = round(float(random.random()*100),2)
			input_function(6)
	else:
		printing(var1, var2, var3, var4, var5, var6)
	    
def printing(a, b, c, d, e, f):
	print("If we use the six numbers entered ", a, ", ", b, ", ", c, ", ",d ,", ",e ,",",f , " as two vectors")
	print(", using calculas we can find the magnitude of the two vectors.")
	print("Magnitude is ", float(magnitude(a, b, c, d, e, f)))

def magnitude(a, b, c, d, e, f):
	mag = math.sqrt(((a-d)**2)+((b-e)**2)+((c-f)**2))
	return mag;
print("This program will ask for six random numbers (if an input is invalid a random number will be selected).")
input_function(0);
