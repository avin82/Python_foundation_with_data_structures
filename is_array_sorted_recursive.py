# PROGRAM is_array_sorted_recursive:

'''
Given an array, check if it is sorted recursively.

Input Format:
Line 1: Integer n (Array size)
Line 2: Array elements (separated by space)

Output Format:
True or False based on whether the array is sorted or not
'''

####################################
# Is Array Sorted Recursive Module #
####################################


def is_array_sorted_recursive(arr):
	if len(arr) == 0 or len(arr) == 1:
	# THEN
		return True
	# ENDIF;
	if arr[0] > arr[1]:
	# THEN
		return False
	# ENDIF;
	return is_array_sorted_recursive(arr[1:])
# END is_array_sorted_recursive.


################
# Main Program #
################

n = int(input("Input the size of array (or list): \n"))
arr = [int(x) for x in input("Input the elements of array (or list, separated by space): \n").split()]
print(is_array_sorted_recursive(arr))
# END.
