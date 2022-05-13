#Daniel De Jesus
# 12/11/2017

#comments---------------------------------

#imports----------------------------------
#input------------------------------------

#functions--------------------------------
def passwrdChecker():
	word = input("Enter password: ")
	retype = input("Please retype password: ")
	if retype == word:
		print("The passwords match!")
	else:
		print("Sorry the passwords do not match.")
		
	

#main-------------------------------------
def main():
	passwrdChecker()
	
main()
