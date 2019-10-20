# PROGRAM sum_of_array_recursive:

'''
Given an array of length N, you need to find and return the sum of all elements of the array.

Do this recursively.

Input Format:
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Output Format:
Sum

Constraints:
1 <= N <= 10^3

Sample Input:
3
9 8 9

Sample Output:
26
'''

#################################
# Sum Of Array Recursive Module #
#################################


def sum_of_array_recursive(arr):
	if len(arr) == 1:
	# THEN
		return arr[0]
	# ENDIF;
	return arr[0] + sum_of_array_recursive(arr[1:])
# END sum_of_array_recursive.


################
# Main Program #
################

n = int(input("Input the size of the array or list: \n"))
arr = [int(x) for x in input("Input the elements of the array or list separated by spaces: \n").split()]
print(sum_of_array_recursive(arr))
# END.
