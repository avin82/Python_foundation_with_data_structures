# PROGRAM print_first_n_natural_numbers_recursive:

'''
Given a number n, print first n natural numbers.

Input Format:
A natural number n

Output Format:
First n natural numbers each number in a separate line
'''

##################################################
# Print First n Natural Numbers Recursive Module #
##################################################


def print_first_n_natural_numbers_recursive(n):
	if n == 0:
	# THEN
		return
	# ENDIF;
	print_first_n_natural_numbers_recursive(n - 1)
	print(n)
# END print_first_n_natural_numbers_recursive.


################
# Main Program #
################

n = int(input("Input a natural number n to print first n natural numbers: \n"))
print_first_n_natural_numbers_recursive(n)
# END.
