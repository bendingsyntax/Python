# Student name: Daniel De Jesus
# Date:12/11/2017
# Python 3.X dev environment

#comments---------------------------------
#This program will read in a file names "sunspots.txt"
#read the data, and write the out put to a "results.txt" file
#with two columns one for the year and the second for the average 
#sunspots for that year
#imports----------------------------------

#input------------------------------------

#functions--------------------------------
def sunspotAvg():
	fh = open("sunspots.txt", 'r')
	totalRead = open("sunspots.txt", 'r')
	rh = open("result.txt", 'w')     #these two lines are for
	rh.close()                       #resetting the results file
	readFile = fh.read()
	splitFile = readFile.split()
	yearList = ["Year"]
	avgSpotList = ["Average Sun Spots"]
	collective = 0
	numYears = 0
	numSpots = 0
	count = 0
	firstAvg = 0
	
	for totals in splitFile:					#This for loop is to count both the 
		if totals.find(".") > -1:				#amount of sunspots and years in the file
			numSpots += 1						
		else:
			numYears += 1
			
	lineRead = totalRead.readline()
	lineReadSplit = lineRead.split()
	
	for x in lineReadSplit:
		if x.find(".") > -1:
			firstAvg += round(float(x),1)
		count += 1
	
	spotsPerLine = (count - 1)
	
	for boolList in splitFile:				#This for loop and nested if statments is to set boolean
		if boolList.find(".") > -1:			#values to determine which list the value will go to
			collective += round(float(boolList),1)			
			bool_ListValue = False
		else:
			bool_ListValue = True
	
		if bool_ListValue != False:
			splitBoolList  = boolList.split()
			avg = round(float(collective / spotsPerLine),1)
			avgSpotList.extend([avg])
			yearList.extend([boolList])
			collective = 0
	
	avgSpotList[1] = round(float(firstAvg / spotsPerLine),1)
		
	with open("result.txt", 'a') as rh:			#This with and for loop are to write to file 
		for x in range((numYears)):				#but using the argument append ('a') 
			lineConvert = "{}	{}"				#so that the file is not over written, as 
			if x == 0:							#well as formatting the string values
				rh.write(lineConvert.format(str(yearList[x]),str(avgSpotList[x])) + "\n")
			else:
				rh.write("\n" + lineConvert.format(str(yearList[x]),str(avgSpotList[x])))
				
	rh.close()

#main-------------------------------------
def main():
	sunspotAvg()
	
main()
