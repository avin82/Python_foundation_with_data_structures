# PROGRAM find_factorial:

'''
Given a number n, find its factorital recursively.

Input Format:
An integer n

Output Format:
Factorial value of n

Sample Input:
5

Sample Output:
120
'''

###################################
# Find Factorial Recursive Module #
###################################


def find_factorial_recursive(n):
	if n == 0:
	# THEN
		return 1
	# ENDIF;
	return n * find_factorial_recursive(n - 1)
# END find_factorial_recursive.


################
# Main Program #
################

n = int(input("Please input the number to find its factorial: \n"))
print(find_factorial_recursive(n))
# END.
