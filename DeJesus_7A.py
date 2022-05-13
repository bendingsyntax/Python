# Student name: Daniel De Jesus
# Date:12/06/2017
# Python 3.X dev environment
# Lesson 7 Programming Assignment A
# Complete the code below by:
# 1. Writing the code to complete each function as described.
# 2. Writing the additional test cases to test the functions.
# ----------------------------------

def withoutX(aStr):
	if (aStr[0] is "x") and (aStr[-1] is "x"):
		return aStr[1:-1]
	elif aStr[0] is "x":
		return aStr[1:]
	elif aStr[-1] is "x":
		return aStr[:-1]
	else:
		return aStr

# ------------------------------------
def frontAgain(aStr):
	if (aStr[0:2] == aStr[-2:]):
		return True
	else:
		return False
	
# ------------------------------------
def doubleChar(aStr):
	doubleVal = ""
	for x in aStr[0:]:
		doubleVal = doubleVal + x + x
	return doubleVal
 
	

def main():
	
	#Testing doubleChar(aStr)
	print("Testing doubleChar(aStr)" )
	assert(doubleChar("hello") == "hheelllloo")
	assert(doubleChar("The") == "TThhee")
	assert(doubleChar("AAbb") == "AAAAbbbb")
	assert(doubleChar("Hi-There") == "HHii--TThheerree")
	assert(doubleChar("Python") == "PPyytthhoonn")
	print("If no Assert errors to this point - doubleChar(aStr) works.")
	print("\n")
	
	#Testing frontAgain(aStr):
	print("Testing frontAgain(aStr)" )
	assert(frontAgain("edited") == True)
	assert(frontAgain("edit") == False)
	assert((frontAgain("ed")) == True)
	assert((frontAgain("emblem")) == True)
	assert((frontAgain("Mark")) == False)
	print("If no Assert errors to this point - frontAgain(aStr) works.")
	print("\n")
	
	#Testing withoutX(aStr):
	print("Testing withoutX(aStr)" )
	assert(withoutX("xHix") == "Hi")
	assert(withoutX("xHi") == "Hi")
	assert(withoutX("Hxix") == "Hxi")
	assert(withoutX("xray") == "ray")
	assert(withoutX("example") == "example")
	print("If no Assert errors to this point - withoutX(aStr) works.")
	
	
	
	
main()
