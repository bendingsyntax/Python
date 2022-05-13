#Daniel De Jesus
# 10/11/2017

#comments---------------------------------
#Exercise 5: Take the following Python code that stores a string:‘
#str = ’X-DSPAM-Confidence:0.8475’
#Use find and string slicing to extract the portion of the string after the colon
#character and then use the float function to convert the extracted string into a
#floating point number.

#imports----------------------------------

#input------------------------------------

#functions--------------------------------
def decimal():
	string = "X-DSPAM-Confidence:0.8475"
	deciStart = string.find(":") + 1
	newString = string[deciStart:]
	deci = float(newString)
	print (deci)
	

#main-------------------------------------
def main():
	decimal()
	
main()
