#!/usr/bin/python3
'''
Christian Chavez 
November 30th 2016
This code takes a string and outputs the frequency of the letters.
'''

def main():
	'''
	This is the main fuction of the program. 
	Initializes the alphabet array
	Read users ciphertext, count the letter frequency, output the letter frequency
	'''
	alpahbet = [0] * 26
	print ("This will count the frequency of letters. Enter ciphertext: ")
	cipherText = input ().lower()
	frequencyCount(cipherText, alpahbet)
	print ("The letter frequency for {} is: ".format(cipherText))
	frequencyOutput(alpahbet)
	exit()


def frequencyCount(text, letterCount):
	'''
	Reads through the string and increments elements in array depending
	on letter read.

	Parameters:
	text -- this is ciphertext that is read through
	letterCount -- this is the alpahbet array that was initalized in the main
	'''
	for letter in text:
		count = ord(letter) - 97
		if count >-1 and count < 27:
			letterCount[count] += 1

def frequencyOutput(letterCount):
	'''
	Outputs every letter in the alpahbet and the number of times each one occured

	Parameter:
	letterCount -- this is the alphabet array that was initalized in the main
	'''
	for var in range(0,26):
		print("{}: {}".format(chr(var+65), letterCount[var]))

if __name__ == "__main__":
    main()