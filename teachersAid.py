#Name:	Malcolm M
#Date:	1/4/21
#Desc:	This code helps teachers bump up their class average by changing
#	six random questions in each students exam. I was inspired by the
#	book Freakonomics where the author described a bunch of teachers
#	who were caught changing a large portion of student test answers.

from string import *
from random import *

#testKey = {} // later version for reading in a filename
testKey = {1:'A', 2:'D', 3:'C', 4:'A', 5:'D', 6:'B', 7:'A', 8:'B', 9:'D', 10:'A', 11:'C', 12:'B', 13:'D', 14:'D', 15:'C', 16:'A', 17:'A', 18:'B', 19:'D', 20:'B'}
tests=[]

#def createKey():
	#return testKey // later version for reading in a file

#prints the key initialized in the program
def printKey():
	print("The test key is:")
	str = ""
	i = 1
	while i in testKey:
		str += testKey[i]
		i += 1
	print(str)
	print()
	return None

#reads each test from a file called grades.txt and creates a list out of them
def readTests():
	try:
		filename = "grades.txt"
		i = 0
		for line in open(filename, "r").readlines():
			line = line.replace('\n', '')
			tests.append(line)
			i+=1
	except IOError:
		print("Cannot read file")
		exit(1)
	return tests		#return a list of student's answers as strings to main

#print the class test answers
def printClass():
	print("The class test answers are:")
	for line in tests:
		print(line)

def main():
	#createKey() // later version for reading in file of test keys
	printKey()		#prints the key being used
	readTests()		#read in the tests from a standard .txt file
	printClass()	#print the array of test values before alteration
	
	#do the altering of test scores in a while loop
	i=0
	randList=[]
	while i < len(tests):
		randList = sample(range(1, 20), 5) #generate random list of numbers
		
		str = tests[i]
		j=0
		#for each value in the array of random numbers, change the test score to the value stored in the dictionary
		for j in randList:	
			firHalf = str[:j-1]
			secHalf = str[j:]
			str = firHalf + testKey[j] + secHalf	#reconstruct str from first half, value in test key, and second half
			j+=1
		tests[i] = str		#add the string back to the array of tests
		i+=1

	#print the class again to determine if it changed correctly
	print()
	printClass()
	return None

main()