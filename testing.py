# Use the file name mbox-short.txt as the file na


#for count in sortList:
 #  	firstWord = sortList(count)
  #  secondWord = sortList(count + 1)
   # if firstWord(0) > secondWord(0) and count < 1:
    #    sortedList = firstWord
     #   sortedList.append(secondWord)
    #elif 
        
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
sortList = []
for line in fh:
    romeoList = line.split()
    sortList.extend(romeoList)

sortedList = sorted(sortList)
abcList = []
count = 0
endList = int(len(sortedList) - 1)
for count in range(endList):
	wordFind = sortedList[count]
	if wordFind in abcList():
		abcList.append(sortedList[count])
	
