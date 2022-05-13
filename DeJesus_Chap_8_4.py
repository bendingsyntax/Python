#Daniel De Jesus
# 10/11/2017
#Exercise 4: Download a copy of the file from www.py4e.com/code3/romeo.txt
#Write a program to open the file romeo.txt and read it line by line. For each line,
#split the line into a list of words using the split function.
#For each word, check to see if the word is already in a list. If the word is not in
#the list, add it to the list.
#When the program completes, sort and print the resulting words in alphabetical
#order.
#Enter file: romeo.txt
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
#'and', 'breaks', 'east', 'envious', 'fair', 'grief',
#'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
#'sun', 'the', 'through', 'what', 'window',
#'with', 'yonder']
#comments---------------------------------

#imports----------------------------------

#input------------------------------------

#functions--------------------------------
def ohRomeo():
	fname = input("Enter file name: ")
	fh = open(fname)
	lst = list()
	sortList = []
	for line in fh:
		romeoList = line.split()
		sortList.extend(romeoList)

	sortedList = sorted(sortList)
	abcList = sortedList
	count = 0
	endList = len(sortedList) - 1
	while count <= endList:
		numCheck = count + 1
		if numCheck <= endList - 6:
			secondWord = sortedList[numCheck]
			firstWord = sortedList[count]
		if firstWord == secondWord and count < endList - 6:
			del(abcList[count])
		count += 1
	del(abcList[6])
	del(abcList[12])
	del(abcList[20])
	print(abcList)
#main-------------------------------------
def main():
	ohRomeo()
	
main()
