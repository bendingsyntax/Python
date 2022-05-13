def doubleChar(aStr):
	doubleVal = ""
	for x in aStr:
		doubleVal = doubleVal + x + x
	return doubleVal
def frontAgain(aStr):
	if (aStr[0:2] == aStr[-2:]):
		return True
	else:
		return False
def withoutX(aStr):
	if (aStr[0] is "x") and (aStr[-1] is "x"):
		return aStr[1:-1]
	elif aStr[0] is "x":
		return aStr[1:]
	elif aStr[-1] is "x":
		return aStr[:-1]
	else:
		return False






def main():
	assert(doubleChar("The") == "TThhee")
	assert(doubleChar("AAbb") == "AAAAbbbb")
	assert(doubleChar("Hi-There") == "HHii--TThheerree")
	assert(frontAgain("edited") == True)
	assert(frontAgain("edit") == False)
	assert((frontAgain("ed")) == True)
	assert(withoutX("xHix") == "Hi")
	assert(withoutX("xHi") == "Hi")
	assert(withoutX("Hxix") == "Hxi")
main()
