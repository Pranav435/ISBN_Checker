"""
This is an addition to our mechanism. In this program, or rather sub-system program, we will be introducing another datatype, files. We will put this into practise by taking the isbn input from a file.
Of course, this is going to be very basic and the file is only allowed to contain the isbn number in order to work.
Again, we will import the isbn module.
"""
import isbn #imports the module
#now we define the function file_isbn_test
def file_isbn_test(): #definition statement
#now we define a few variables that our function will use.
	fhand="" #our file handle
	file_input="" #variable to store the name of the file
	result=0 #variable that will hold the result of our program
	isbn_int=0 #integer version of our isbn number
	isbn_string="" #the string that will hold the coersed version of our number
	correct=False #flag that we will use when taking input
#now we get into the input
#we will, as usual, take input using a while loop so as to let the user try again if there was an error.
	while correct==False: #our while loop definition
		try:
			file_input=input("Enter the name of the file to open: ") #this is our input function
			fhand=open(file_input) #this will open the file in read mode
		except: #if there was an error in opening the file
			print("Oops. Looks like that file either does not exist or can't be opened at this moment. Please try again.") #appropriate error message
			continue #we let the user try again
#the following lines will only execute if the above try except block does not return an error and the user has entered a valid file name.
#now, we need to get the number from the file and then input it to the function. We also need to check if it is a valid isbn number.
#to do this, we use the read method of the file data structure.

		isbn_string=fhand.read() #gets the number from the file
#now, we have another try_except block to check if the coersion from string to int is actually possible.
		try:
			isbn_int=int(isbn_string) #coerses the string to an integer
		except: #what happens if things go wrong
			print("Oops! That file does not contain an integer that can be fed to the function! Please try again!") #error message
			continue #we have the user go all the way from the start to enter the file name again.

#The following lines will only be executed if the above try except block did not catch any errors, I.E, the coersion was successful.
#now we need to assess if the number fetched is of the isbn format, which, as you know, is a 13 digit positive integer. If you have looked at the basic_isbn_test.py file, you will be familiar with the way we do this. If not then:
#We use the error codes given in isbn.py to check if the number is of the isbn format. Please refer to the isbn.py file to know what each error code means. First, though, we will have to run the number through the function to get output.
		result=isbn.isbn_check(isbn_int) #we run the number through the function and store the return value in result
#now, we use the first error code to check if the number is positive
		if result==-1: #the first error code
			print("Oops. The number entered is not a positive number. Please correct this and try again.") #appropriate error message
			continue #we let the user try again
		if result==-2: #number too short or too long
			print("Oops! Your number is not of the length of an isbn number, which is supposed to be 13 digits long. Please correct this and try again.") #appropriate error message
			continue #we let the user try again

#the following line will only execute if all the above tests do not catch errors, I.E, the user has entered a valid isbn number through the file.
		correct=True

#we're almost done with our venture into the file world. All we have to do now is run the number through the function again and seee if it is valid.
	result=isbn.isbn_check(isbn_int) #we run the input again through the function just to be safe
#now we check the answer using conditionals.
	if result==True: #the number is valid
		print("Congratulations! The ISBN number entered is valid!") #message
	else: #the number is invalid
			print("Oops. The ISBN number entered is invalid.") #message