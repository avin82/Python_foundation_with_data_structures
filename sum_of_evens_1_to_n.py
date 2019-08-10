# PROGRAM sum_of_evens_1_to_n:

#######################
# Sum Of Evens Module #
#######################


def sum_of_evens_1_to_n_inclusive():
	n = int(input("Input the number to find sum of evens between 1 and the entered number (both inclusive): \n"))
	sum = 0
	while n != 0:
	# DO
		num = int(input("Enter the number: \n"))
		if num % 2 == 0:
		# THEN
			sum = sum + num
		# ENDIF;
		n = n - 1
	# ENDWHILE;
	return sum
# END sum_of_evens_1_to_n_inclusive.


################
# Main Program #
################

print(sum_of_evens_1_to_n_inclusive())
