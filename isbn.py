#the following function, when given an ISBN number, that is, a positive integer which is 13 digits long, will check its validity using the following algorithm
#algorithm:
"""
Step 1. Add up all the odd_positioned digits. That is: odd_total=isbn[0]+isbn[2]+isbn[4]+isbn[6]+isbn[8]+isbn[10]+isbn[12]
Step 2: Add up all the evenly positioned digits, that is, even_total=isbn[1]+isbn[3]+isbn[5]+isbn[7]+isbn[9]+isbn[11], and multiply the result by 3: even_total*=3
Step 3: Add the totals from steps 1 and 2: total=odd_total+even_total
step 4: If the remainder between the total and 10 is 0, then the number is valid. Else, it is not: if total%10==0: True. Else: False.
This happens because the last digit in the number is a check digit. Each ISBN number has a unique check digit that identifies its validity. If the remainder is not 0, then the check digit is invalid, and thus, the ISBN number is invalid.
"""
#Note: the function isbn_check(isbn_number), is only a module. You can import it into your program by saying import isbn or from isbn import isbn_check.
"""
isbn_check
Input: an ISBN number, that is, a 13 digit non-negative number.
Output: True if the number is valid, False if it is not.
Error codes:
-1: Negative number.
-2: Number too short or too long.
"""

def isbn_check(isbn_number):

#the following few lines are declarations of variables that our function will then use.
	isbn=[] #the list on which the main validity check of the ISBN number will take place
	odd_total=0 #an auxiliary variable that will help in the validity check
	even_total=0 #another auxiliary variable
	total=0 # a third auxiliary or helper variable that will help in step 3 of the algorithm.
	isbn_string=str(isbn_number) # this variable will be useful in setting up the above isbn list for the operation, but will not have any other use.
	i=0 # this is our itteration variable throughout the function

#the following few conditionals perform tests to seee if the number passed as a parameter is in the format of an ISBN number, that is a 13 digit positive integer.	
	if isbn_number<=0: # this checks to see if the number is a positive integer
		return -1 # our error code.

	if len(isbn_string)<13 or len(isbn_string)>13: # this checks the length of the number, which has to be 13 characters
		return -2 # error code

#Converting the stringified isbn number to a list of strings
	for char in isbn_string:
		isbn.append(char)

#the following snippet converts our list into a list of integers, which can then be processed to check validity.
	i=0
	while i<13:
		isbn[i]=int(isbn[i])
		i+=1
#the following loops add up the numbers, all except the check digit.
#first, i is initialized to 0
	i=0
	while i<13:
		odd_total+=isbn[i]
		i+=2

#re-initializing the variable i to 1, as we are now adding up even numbers
	i=1
	while i<=12:
		even_total+=isbn[i]
		i+=2

# the following line makes a change to our even_total variable so that the processing can be done right
	even_total*=3

#the following line adds up both the totals
	total=odd_total+even_total

#now, the final check is implemented
	if total%10==0:
		return True
	else:
		return False