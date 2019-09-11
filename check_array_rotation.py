# PROGRAM check_array_rotation:

'''
Given an integer array, which is sorted (in increasing order) and has been rotated by some number k in clockwise direction. Find and return the k.

Input format:
Line 1 : Integer n (Array Size)
Line 2 : Array elements (separated by space)

Output Format:
Integer k

Constraints :
1 <= n <= 1000

Sample Input 1:
6
5 6 1 2 3 4

Sample Output 1:
2

Sample Input 2:
5
3 6 8 9 10

Sample Output 2:
0
'''

###############################
# Check Array Rotation Module #
###############################


def check_array_rotation(arr):
	for i in range(1, len(arr)):
	# DO
		if arr[i] < arr[i - 1]:
		# THEN
			return i
		# ENDIF;
	# ENDFOR;
	else:
		return 0
# END check_array_rotation.
	

################
# Main Program #
################

n = int(input("Input the size of array (or list): \n"))
arr = [int(x) for x in input("Input the elements of array (or list, separated by space): \n").split()]
print(check_array_rotation(arr))
# END.

