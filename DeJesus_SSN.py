#Daniel De Jesus
# 12/11/2017

#comments---------------------------------

#imports----------------------------------

#input------------------------------------

#functions--------------------------------
def socialSecurity():
	ssn = input("Please enter a social security number with dashes: ")
	if ssn[3] == "-" and ssn[6] == "-" :
		print("This is a valid social security number.")
	else:
		print("That is not a valid social security number")
		print("please make sure that only numbers and dashes are used")
		print("example: 123-45-6789 ")

#main-------------------------------------
def main():
	socialSecurity()
	
main()
