#!/usr/bin/python3
'''
Christian Chavez 
November 30th 2016
Using Ceaser Cipher this code encryptes a string given a key or outputs 
every possible decryption given the ciphertext.
'''
def main():
	'''
	This is the main fucntion of the program.
	Give the user the option to encrypt or decrypt. 
	If encrypt read key size then text and run encrypt function
	Else if decrypt read cipher text and run decrypt function
	If invalid input output error.
	'''
	print ("This will encrypt or decrypt using a ceaser cipher.");
	choice = input("Would you like to 1) Encrypt or 2) Decrypt: \n").lower();
	if choice == '1' or choice == 'encrypt' or choice == '-e' or choice == 'e':
		encrypt(int(input("Enter a shift key for the encryption: \n")), input("Now enter the message you want to Encrypt: \n"));
	elif choice == '2' or choice == 'decrypt' or choice == '-d' or choice == 'd':
		text = input("Now enter the message you want to Decrypt: \n")
		print ("Decryptions for {} are: ".format(text))
		decrypt(text)
	else: print ("Error, unknown input.")
	exit();

def encrypt(key, string):
	'''
	This function is used to encrypt text given a key using ceaser cipher.
	If the key is a negative number output value error
	Otherwise increase each letter by the key size.
	Output the ciphertext

	Parameters:
	key -- this is the key size to incrment each char in the string by.
	string -- this is the original text that is turned into ciphertext.
	'''
	if key < 0:
		raise ValueError
	newMessage = '';
	for num, letter in enumerate (string):
		for counter in range(0,key):
			if ord(letter) == 90:
				letter = 'A';
			elif ord(letter) == 122:
				letter = 'a';
			elif ord(letter)>122 or (ord(letter)<97 and ord(letter)>90) or ord(letter)<64:
				letter = letter;
			else:
				letter = chr(ord(letter)+1);
		newMessage += letter;
	print ("Encrypted text: {}".format(newMessage))

def decrypt(string):
	'''
	This function is used to decrypt the ciphertext Using ceaser cipher.
	Iterates 25 times. Once for every letter in the alphabet. 
	Read through the string and increase each valid letter by one. 
	Output the updated string. Repeat 

	Parameters:
	string -- This is the string that is read through 
	'''
	for var in range(0,25):
		newMessage = '';
		for num, letter in enumerate (string):
			if ord(letter) == 90:
				letter = 'A';
			elif ord(letter) == 122:
				letter = 'a';
			elif ord(letter)>122 or (ord(letter)<97 and ord(letter)>90)or ord(letter)<64:
				letter = letter;
			else:
				letter = chr(ord(letter) + 1);
			newMessage += letter;
		string = newMessage
		print (string)

if __name__ == "__main__":
    main()

