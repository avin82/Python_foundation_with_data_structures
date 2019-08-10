# PROGRAM largest_of_three:

#######################
# Find Largest Module #
#######################


def find_largest():
	num1 = int(input("Input first number: \n"))
	num2 = int(input("Input second number: \n"))
	num3 = int(input("Input third number: \n"))

	if num1 >= num2:
	# THEN
		if num1 >= num3:
		# THEN
			print("{} is the largest amongst the user inputted numbers.".format(num1))
		else:
			print("{} is the largest amongst the user inputted numbers.".format(num3))
		# ENDIF;
	elif num2 >= num3:
	# THEN
		print("{} is the largest amongst the user inputted numbers.".format(num2))
	else:
		print("{} is the largest amongst the user inputted numbers.".format(num3))
	# ENDIF;
# END find_largest.


################
# Main Program #
################

find_largest()
