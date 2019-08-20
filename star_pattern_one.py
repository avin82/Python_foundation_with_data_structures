# PROGRAM star_pattern_one:

'''
Write a program to take a number input from user. Let's say the user inputs the number 4, then the program should print the following pattern (for n = 4):

****
****
****
****
'''

#############################
# Print Star Pattern Module #
#############################


def print_star_pattern():
	n = int(input("Input the number of rows which is equal to the number of columns to print the desired star pattern: \n"))
	i = 1
	while i <= n:
	# DO
		j = 1
		while j <= n:
		# DO
			print("*", end="")
			j = j + 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_star_pattern.


################
# Main Program #
################

print_star_pattern()
# END.
