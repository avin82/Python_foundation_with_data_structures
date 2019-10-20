# PROGRAM find_nth_fibonacci_recursive:

'''
Given a number n, find the nth fibonacci number.

Input Format:
A natural number n

Output Format:
nth fibonacci number

Sample Input:
4

Sample Output:
3
'''

#######################################
# Find nth Fibonacci Recursive Module #
#######################################


def find_nth_fib_recursive(n):
	if n == 1 or n == 2:
	# THEN
		return 1
	# ENDIF;
	return find_nth_fib_recursive(n - 2) + find_nth_fib_recursive(n - 1)
# END find_nth_fib_recursive.


################
# Main Program #
################

n = int(input("Input a natural number n to find the nth fibonacci number: \n"))
print(find_nth_fib_recursive(n))
# END.
