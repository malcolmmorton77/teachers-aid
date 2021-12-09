#Name:	Malcolm M
#Date:	1/4/21
#Desc:	This code helps teachers bump up their class average by changing
#	six random questions in each students exam. I was inspired by the
#	book Freakonomics where the author described a bunch of teachers
#	who were caught changing a large portion of student test answers.

from string import *

testLength = 20
#testKey = {} // later version for reading in a filename
testKey = {1:'A', 2:'D', 3:'C', 4:'A', 5:'D', 6:'B', 7:'A', 8:'B', 9:'D', 10:'A', 11:'C', 12:'B', 13:'D', 14:'D', 15:'C', 16:'A', 17:'A', 18:'B', 19:'D', 20:'B'}
testConverter = {1:'A', 2:'B', 3:'C', 4:'D'}
arr=[]

#def createDict():
	#return testKey // later version for reading in a file

def printKey():
	print("The test key is:")
	str = ""
	i = 1
	while i<=testLength:
		str += testKey[i]
		i += 1
	print(str)
	return None

def readTests():
	try:
		filename = "grades.txt"
		i = 0
		for line in open(filename, "r").readlines():
			line = line.replace('\n', '')
			arr.append(line)
			i+=1
	except IOError:
		print("Cannot read file")
	return arr		#return a list of strings to main

def printClass():
	for line in arr:
		print(line)

def main():
	#createDict() // later version for reading in file of test keys
	printKey()		#prints the key being used
	readTests()		#read in the tests from a standard .txt file
		#print the array of test values before alteration
	printClass()
	#do the altering of test scores
	#algorithm to create n different random numbers
	#for each value in the array of random numbers
	#change the test score to the value stored in the dictionary
	#REMEMBER: the array value is going to be off by one from dict
	#add the string back to the array of tests
	#print the class again to determine if it changed correctly
	return None

main()

#Answer string is the students answers in numerical order from 1 to testLength
#for one test as a string
#Store the given Answer string in a variable
#create 6 random numbers from 1 to numQuestions
#store the six random variables in an array
#these are the six questions which will have their answers changed
#Inside a loop, change the six questions by using the dictionary
#and altering the answer string
#1.A letter indicates the student answered it correctly and can be skipped
#2.A number indicates the student answered with the incorrect answer
#3.A 0 indicates it was left blank

#For cases 2&3, find dictionary mapping for that question using the position in
#the character array and altering using the respective dicitonaries

#print out the new string

#Inside a function:
#create a dictionary and enumerate each of 1 through numQuestions
#with the correct answer for this fictitious test
#create a smaller dictionary mapping 1="A", 2="B", 3="C", 4="D" for conversions
#return to main
