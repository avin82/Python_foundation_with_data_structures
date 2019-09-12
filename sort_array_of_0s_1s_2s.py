# PROGRAM sort_array_of_0s_1s_2s:

'''
You are given an integer array containing only 0s, 1s and 2s. Write a solution to sort this array using one scan only.

You need to change in the given array itself. So no need to return or print anything.

Input format:
Line 1 : Integer n (Array Size)
Line 2 : Array elements (separated by space)

Output Format:
Updated array elements (separated by space)

Constraints :
1 <= n <= 10^6

Sample Input:
7
0 1 2 0 2 0 1

Sample Output:
0 0 0 1 1 2 2
'''

#####################################
# Sort Array of 0s 1s and 2s Module #
#####################################


def sort_array_of_0s_1s_2s(arr):
	i, next_zero, next_two = 0, 0, len(arr) - 1
	while i <= next_two:
	# DO
		if arr[i] == 0:
		# THEN
			arr[next_zero], arr[i] = arr[i], arr[next_zero]
			next_zero = next_zero + 1
			i = i + 1
		elif arr[i] == 2:
		# THEN
			arr[next_two], arr[i] = arr[i], arr[next_two]
			next_two = next_two - 1
		else:
			i = i + 1
		# ENDIF;
	# ENDWHILE;
# END sort_array_0s_1s_2s.


################
# Main Program #
################

n = int(input("Input the size of array (or list): \n"))
arr = [int(x) for x in input("Input the elements of array (or list, separated by space): \n").split()]
sort_array_of_0s_1s_2s(arr)
print(*arr)
# END.
