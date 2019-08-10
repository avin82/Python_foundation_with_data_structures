# PROGRAM find_gcd:

###################
# Find GCD Module #
###################


def find_gcd():
	num1 = int(input("Input the first number to find gcd: \n"))
	num2 = int(input("Input the second number to find gcd: \n"))
	counter = 1
	while (counter <= num1) and (counter <= num2):
	# DO
		if (num1 % counter == 0) and (num2 % counter == 0):
		# THEN
			gcd = counter
		# ENDIF;
		counter = counter + 1
	# ENDWHILE;
	return gcd
# END find_gcd.


################
# Main Program #
################

print("Gcd of user inputted numbers is {}".format(find_gcd()))
