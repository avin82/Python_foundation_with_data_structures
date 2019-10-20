# PROGRAM print_n_to_1_recursive:

'''
Given a number n, print numbers n to 1.

Input Format:
A natural number n

Output Format:
Numbers n to 1 each number in a separate line
'''

#######################
# Print n To 1 Module #
#######################


def print_n_to_1_recursive(n):
	if n == 0:
	# THEN
		return
	# ENDIF;
	print(n)
	print_n_to_1_recursive(n - 1)
# END print_n_to_1_recursive.


################
# Main Program #
################

n = int(input("Input a natural number n to print numbers n to 1: \n"))
print_n_to_1_recursive(n)
# END.
