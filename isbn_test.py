"""
This program tests our isbn_check module. The code for that function can be found in the isbn.py file attached.
This program will also show exception handling and importing.
To get the isbn_check function, we have to import it.
We can do that in two ways.
Note, however, that we have to import it in the first few lines of our code. The length of the import section depends upon how many modules are being imported.
To import, we can either write
import isbn
Thus, the whole isbn module will be imported. That means that whatever variables, functions, classes, statements and code written in isbn.py will be accessible to this current file.
We can also be more specific and write
from isbn import isbn_check
This will only import the data in the isbn_check function in the isbn.py file. This is useful if we want to import one function from a huge code file with many functions, classes and variable definitions.
Note that in this example, I usually like to use the first method of immporting, and that is what will be used here. Feel free to play around with the code and modify it to use the second one.
"""

import isbn # we import our module
#now we declare a few global variables
result=0 # this stores the end-result
correct=False # this is a flag that we will use shortly, when we take the input from the user. Keep reading to find out how it is used.
isbn_input=0 # this is the variable that will hold the user's input
# now we define a loop in which we take the isbn number from the user. We put it in a loop so that, if an error were to occur, it would show the appropriate message and let the user try again.
while correct!=True: #here's where the correct flag is used. We say correct!=True, which means that the value of correct can be anything but True.
	try: #this is the main try block. This is the first test that we perform. The reason we have a try block is that we can figure out if the user has entered a string and not have the program display a traceback error, which is not user-friendly, but more importantly, a huge security risk.
		isbn_input=int(input("Enter an ISBN number: ")) #we take the input from the user
	except: # this block will define what the program should do if an exception occurs.
		print("Oops. Invalid input. Please enter an ISBN number, which is an integer.") #this is our error message
		continue #we let the user try again
#the following lines of code will only execute if the user enters an integer.
#the following tests will ensure that the user enters a number in the ISBN format, which is a 13 digit positive integer.

#To do this, we use the error codes in the isbn.pyy file. Please refer to that file to learn more. First though, to get at the values, we run the isbn_input variable through the isbn_check function
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
#the final part of our venture is to print the appropriate messages.
if result==True: #the number is valid
	print("Congratulations! The ISBN number is Valid!") #appropriate message
else:
	print("Oops. The number is not valid. Please check the ISBN number and try again.") #appropriate error message

"""
Final Notes:
Congratulations!
We have come to our venture. We now have a working and well oiled implementation of our algorithhm.
Feel free to play around with the code and try to change things about.
If in doubt, don't forget to E-Mail me at
pranavsavla2003@gmail.com
to discuss the problem.
Thanks for staying with me!
"""