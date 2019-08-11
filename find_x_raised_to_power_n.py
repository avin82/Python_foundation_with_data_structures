# PROGRAM find_x_raised_to_power_n:

'''
You are given two integers: X and N. You have to calculate X raised to power N and print it.

Input format:
The first line of input contains an integer X (1 <= X <= 100)
The second line of input contains an integer N (1 <= N <= 10)

Constraints:
Time Limit: 1 second

Output format:
The first and only line of output contains the result.

Sample Input:
10
4

Sample Output:
10000
'''

###################################
# Find x Raised To Power n Module #
###################################


def find_x_raised_to_power_n_val():
	x = int(input("Input a number to calculate the raised to power function applied to the entered number: \n"))
	n = int(input("Input the raised to power value for the previously entered number to calculate the result: \n"))
	return x ** n


################
# Main Program #
################

print(find_x_raised_to_power_n_val())
# END.
