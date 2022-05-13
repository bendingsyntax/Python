#Daniel De Jesus
#09/28/17

#Exercise 5: What will the following Python program print out?
#4.14. EXERCISES 55
#def fred():
#print("Zap")
#def jane():
#print("ABC")
#jane()
#fred()
#jane()

#a) Zap ABC jane fred jane
#b) Zap ABC Zap
#c) ABC Zap jane
#d) ABC Zap ABC
#e) Zap Zap Zap

def fred():
	print("Zap")
def jane():
	print("ABC")
jane()
fred()
jane()

#Answer is 'd' ABC Zap ABC.
