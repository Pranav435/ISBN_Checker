"""
This is the file that will have the code for our basic isbn test function.
This is not a modular function, meaning that it can not be used on its own.
We will be importing this in the main.py file.
However, for this function to work, we have to import one sub module, which is the isbn module, the code for which can be found in isbn.py.
To do this, we can write the code in two ways:
import isbn will import the whole isbn module, including any functions, variable definitions, classes, and data structures in it.
We could also write
from isbn import isbn_check
This will only import the isbn_check function, ignoring any other definitions in the file.
This file will have the basic_isbn_test function only.
"""
import isbn #we import the module
def basic_isbn_test(): #this is the defining statement.
#now we define a few global variables.
	result=0 # this stores the end-result
	correct=False # this is a flag that we will use shortly, when we take the input from the user. Keep reading to find out how it is used.
	isbn_input=0 # this is the variable that will hold the user's input
# now we define a loop in which we take the isbn number from the user. We put it in a loop so that, if an error were to occur, it would show the appropriate message and let the user try again.
	while not correct: #here's where the correct flag is used. We say not correct because we basically say our flag should not be true. not correct is just a shorthand for correct!=True.
		try: #this is the main try block. This is the first test that we perform. The reason we have a try block is that we can figure out if the user has entered a string and not have the program display a traceback error, which is not user-friendly, but more importantly, a huge security risk.
			isbn_input=int(input("Enter an ISBN number: ")) #we take the input from the user
		except: # this block will define what the program should do if an exception occurs.
			print("Oops. Invalid input. Please enter an ISBN number, which is an integer.") #this is our error message
			continue #we let the user try again
#the following lines of code will only execute if the user enters an integer.
#the following tests will ensure that the user enters a number in the ISBN format, which is a 13 digit positive integer.

#To do this, we use the error codes in the isbn.py file. Please refer to that file to learn more. First though, to get at the values, we run the isbn_input variable through the isbn_check function
		result=isbn.isbn_check(isbn_input) #runs the variable through the function and stores the result in result
		if result==-1: #the number is not positive.
			print("Oops. The ISBN number is not a positive integer. Please enter a positive integer and try again.") #appropriate error message
			continue #we let the user try again
#the following lines will only execute  if the above if condition has completed.
		if result==-2: #number too short or too long
			print("Oops. The number is not of the ISBN format, which is a 13 digit positive number. Please check the length of the ISBN number and try again.") #error message
			continue #we let the user try again
#the following line only executes if all the above conditions return false, or if the user has entered a valid ISBN number.
		correct=True #we exit the loop

#Now, to be safe, we run the variable isbn_check through the function again.
	result=isbn.isbn_check(isbn_input) #now we run the isbn_input variable through the function to check the validity.
#the final part of our venture, in this function, is to print the appropriate messages.
	if result==True: #the number is valid
		print("Congratulations! The ISBN number is Valid!") #appropriate message
	else:
		print("Oops. The number is not valid. Please check the ISBN number and try again.") #appropriate error message