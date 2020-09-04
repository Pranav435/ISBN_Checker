"""
We're almost at the end of our venture.
In this file, as the name might suggest, we control the flow of the program, based on the user's options.
We will be primmarily using all the modules we just made, including the isbn, basic_isbn_test, and file_isbn_test modules.
This file will import 4 other files.
The last one is the time module, a module not designed by us but which is present in the python modules and can be used.
"""
import isbn # the main isbn.py file
import basic_isbn_test #the basic test file, which just takes input and returns if the isbn number is valid
import file_isbn_test #this module takes a file as input and returns if the isbn number within it is valid or not
import time #this lets us use a few time-related functions, the one we'll be using is sleep.
#let's first define a few global variables.
choice="" #this variable will store the user's choice
#now we will set up a basic CLI, or command line interface, where the user can either type b to initiate the basic isbn test, or f to initiate the file isbn test.
#First, though, we need to print a welcome message to the console
print("Welcome to this ISBN checker tool. This tool, when given an ISBN number either by basic CLI input or by a file, will return its validity.")
#now we initiate a while loop which will take the input from the user
while True: #our input loop, or driver loop
	choice=input("Enter b to initiate the basic CLI input method of the ISBN number, f to initiate the file input method of the ISBN number, or e to exit: ") #the CLI input field
#now we use a series of conditional statements to check the user's input
	if choice=="b" or choice=="B": #basic input
		basic_isbn_test.basic_isbn_test() #the basic_isbn_test function
		time.sleep(1) #puts the program to sleep for 1 second, allowing the user to read the output, and also giving the computer a bit of breathing room
		choice="" #re-initializes the choice variable, ready for use by the user

#second condition
	elif choice=="f" or choice=="F": #file input
		file_isbn_test.file_isbn_test() #this initiates the file_isbn_test function
		time.sleep(1) #we wait for the user to read the output and the computer to breathe
		choice="" #we re-initialize the choice variable

#third condition
	elif choice=="e" or choice=="E": #the user chose to exit
		print("Exitting.") #prints a quick exit message
		time.sleep(1) #puts the program to sleep one last time, letting the compiler collect garbage
		break #breaks out of the loop, exitting the program

#last condition
	else: #the user has entered an invalid input
		print("Oops. " + choice + " is not a valid option. Please try again.") #prints the error message
		time.sleep(1) #gives the engine time to collect garbage
		choice="" #re-initializes the choice variable
		continue # we let the user try again.

"""
Final Notes:
Congratulations!
We have come to our venture. We now have a working and well oiled implementation of our algorithm, which also tests with files.
Feel free to play around with the code and try to change things about.
If in doubt, don't forget to E-Mail me at
pranavsavla2003@gmail.com
to discuss the problem, or put a github issue.
Thanks for staying with me!
"""