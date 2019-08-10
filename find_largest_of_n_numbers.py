# PROGRAM find_largest_of_n_numbers:

#######################
# Find Largest Module #
#######################

import math


def find_largest_of_n_numbers():
	n = int(input("Input from how many numbers do you wish to find the largest number: \n"))
	max = -(math.inf)
	while n != 0:
	# DO
		num = int(input("Input the number: \n"))
		if num >= max:
		# THEN
			max = num
		# ENDIF;
		n = n - 1
	# ENDWHILE;
	return max
# END find_largest_of_n_numbers.


################
# Main Program #
################

num_largest = find_largest_of_n_numbers()
print("Largest number amongst the user inputted numbers is {}".format(num_largest))
# END.
