# PROGRAM check_num_in_array_recursive:

'''
Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.

Do this recursively.

Input Format:
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x

Output Format:
true or false

Constraints:
1 <= N <= 10^3

Sample Input:
3
9 8 10
8

Sample Output:
true
'''

#######################################
# Check Num In Array Recursive Module #
#######################################


def check_num_in_array_recursive(arr, num):
	if len(arr) == 1:
	# THEN
		return arr[0] == num
	# ENDIF;
	return (arr[0] == num) or check_num_in_array_recursive(arr[1:], num)
# END check_num_in_array_recursive.


################
# Main Program #
################

n = int(input("Input the size of array (or list): \n"))
arr = [int(x) for x in input("Input the elements of array (or list, separated by space): \n").split()]
num = int(input("Input the number to be searched for in the array provided above: \n"))
if check_num_in_array_recursive(arr, num):
# THEN
	print('true')
else:
	print('false')
# ENDIF;
# END.
