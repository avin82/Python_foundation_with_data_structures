# PROGRAM rotate_array:

'''
Given a random integer array of size n, write a function that rotates the given array by d elements (towards left).

Change in the input array itself. You don't need to return or print elements.

Input format:
Line 1 : Integer n (Array Size)
Line 2 : Array elements (separated by space)
Line 3 : Integer d

Output Format:
Updated array elements (separated by space)

Constraints :
1 <= N <= 1000
1 <= d <= N

Sample Input:
7
1 2 3 4 5 6 7
2

Sample Output:
3 4 5 6 7 1 2
'''

#######################
# Rotate Array Module #
#######################


def rotate_array(arr, d):
	new_tail = arr[:d]
	for i in range(d, len(arr)):
	# DO
		arr[i - d] = arr[i]
	# ENDFOR;
	for i in range(d):
	# DO
		arr[i - d] = new_tail[i]
	# ENDFOR;
# END rotate_array(arr, d).


n = int(input("Input the size of array (or list): \n"))
arr = [int(x) for x in input("Input the elements of array (or list, separated by space): \n").split()]
d = int(input("Input the number of elements (positive integer value) by which the array (or list) needs to be rotated towards the left: \n"))
rotate_array(arr, d)
print(*arr)
# END.
