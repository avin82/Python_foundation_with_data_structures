# PROGRAM sum_of_n_natural_numbers_recursive:

'''
Find sum of first n natural numbers recursively.

Input Format:
An integer n

Output Format:
Sum value of first n natural numbers

Sample Input:
5

Sample Output:
15
'''

#############################################
# Sum Of n Natural Numbers Recursive Module #
#############################################


def sum_of_n_natural_numbers_recursive(n):
	if n == 0:
	# THEN
		return 0
	# ENDIF;
	return n + sum_of_n_natural_numbers_recursive(n - 1)
# END sum_of_n_natural_numbers_recursive.


################
# Main Program #
################

n = int(input("Input a natural number n to find the sum of first n natural numbers: \n"))
print(sum_of_n_natural_numbers_recursive(n))
# END.
