# PROGRAM find_second_largest_in_array:

'''
Given a random integer array of size n, find and return the second largest element present in the array.

If n <= 1 or all elements are same in the array, return -2147483648 i.e. -2^31.

Input format:
Line 1 : Integer n (Array Size)
Line 2 : Array elements (separated by space)

Output Format:
Second largest element

Constraints :
1 <= N <= 10^6

Sample Input 1:
7
2 13 4 1 3 6 28

Sample Output 1:
13

Sample Input 2:
5
9 3 6 2 9

Sample Output 2:
6

Sample Input 3:
2
6 6

Sample Output 3:
-2147483648
'''

#######################################
# Find Second Largest In Array Module #
#######################################


def find_second_largest_in_array(arr):
	if len(arr) <= 1:
	# THEN
		return - 2 ** 31
	else:
		diff = 0
		is_diff = True
		for i in range(1, len(arr)):
		# DO
			if arr[i - 1] - arr[i] != diff:
			# THEN
				is_diff = False
			# ENDIF;
		# ENDFOR;
		if is_diff:
		# THEN
			return - 2 ** 31
		# ENDIF;
	# ENDIF;
	
	largest, second_largest = - float("inf"), - float("inf")
	for i in range(len(arr)):
	# DO
		if arr[i] > largest:
		# THEN
			largest, second_largest = arr[i], largest
		elif arr[i] != largest and arr[i] > second_largest:
		# THEN
			second_largest = arr[i]
		# ENDIF;
	# ENDFOR;
	return second_largest
# END find_second_largest_in_array.


################
# Main Program #
################

n = int(input("Input the size of array (or list): \n"))
arr = [int(x) for x in input("Input the elements of array (or list, separated by space): \n").split()]
print(find_second_largest_in_array(arr))
# END.
