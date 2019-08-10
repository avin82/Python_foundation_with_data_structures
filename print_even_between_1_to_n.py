# PROGRAM print_even_between_1_to_n:

#####################
# Print Even Module #
#####################


def print_even_till_num_inclusive():
	num = int(input("Input number to print all the even numbers between 1 and the entered number both inclusive: \n"))
	start = 1
	while start <= num:
	# DO
		if start % 2 == 0:
		# THEN
			print(start)
		# ENDIF;
		start = start + 1
	# ENDWHILE;
# END print_even_till_num_inclusive.


################
# Main Program #
################

print_even_till_num_inclusive()
