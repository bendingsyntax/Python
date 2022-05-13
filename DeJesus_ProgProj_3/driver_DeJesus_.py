#Daniel De Jesus
# 12/3/17

#comments---------------------------------

#imports----------------------------------

#input------------------------------------

#functions--------------------------------
def readWrite():
	fh = open("data.txt")
	fullFile = fh.read()
	splitFile = fullFile.rsplit()
	upperList = fullFile.upper()
	upperSplit = upperList.split()
	lowerList = fullFile.lower()
	lowerSplit = lowerList.split()
	totalList = len(splitFile)
	twoLetters = 0
	threeLetters = 0
	fourLetters = 0
	fiveLetters = 0
	sixLetters = 0
	sevenLetters = 0
	eightLetters = 0
	nineLetters = 0
	tenLetters = 0
	wordsGreater = 0
	total = 0
	count = 0
	for line in splitFile:
		wordLength = len(line)
		if wordLength == 2:
			twoLetters += 1
		elif wordLength == 3:
			threeLetters += 1
		elif wordLength == 4:
			fourLetters += 1
		elif wordLength == 5:
			fiveLetters += 1
		elif wordLength == 6:
			sixLetters += 1
		elif wordLength == 7:
			sevenLetters += 1
		elif wordLength == 8:
			eightLetters += 1
		elif wordLength == 9:
			nineLetters += 1
		elif wordLength == 10:
			tenLetters += 1
		elif wordLength == 11:
			wordsGreater += 1
		total += wordLength
		count += 1
	
	results = open("result.txt", 'w')
	results.write(str(twoLetters) + " words of length 2\n")
	results.write(str(threeLetters) + " words of length 3\n")
	results.write(str(fourLetters) + " words of length 4\n")
	results.write(str(fiveLetters) + " words of length 5\n")
	results.write(str(sixLetters) + " words of length 6\n")
	results.write(str(sevenLetters) + " words of length 7\n")
	results.write(str(eightLetters) + " words of length 8\n")
	results.write(str(nineLetters) + " words of length 9\n")
	results.write(str(tenLetters) + " words of length 10\n")
	results.write(str(wordsGreater) + " words of length 11\n")
	results.write(str(totalList) + " is the total number of words\n")
	
	upperResults = ""
	for line2 in upperList:
		upperResults += line2
	lowerResults = ""
	for line3 in lowerList:
		lowerResults += line3
	finalUpper = open("uppercase.txt",'w')
	finalLower = open("lowercase.txt",'w')
	finalUpper.write(str(upperResults))
	finalLower.write(str(lowerResults))
	
#main-------------------------------------
def main():
	readWrite()
	
main()
