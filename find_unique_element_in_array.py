# PROGRAM find_unique_element_in_array:

'''
Given an integer array of size 2N + 1. In this given array, N numbers are present twice and one number is present only once in the array.

You need to find and return that number which is unique in the array.

Note : Given array will always contain odd number of elements.

Input format:
Line 1 : Array size i.e. 2N+1
Line 2 : Array elements (separated by space)

Output Format:
Unique element present in the array

Constraints :
1 <= N <= 10^3

Sample Input:
7
2 3 1 6 3 6 2

Sample Output:
1
'''

##############################
# Find Unique Element Module #
##############################


def find_unique_element(li):
	for i in range(len(li)):
	# DO
		if (li[i] not in li[:i]) and (li[i] not in li[i + 1:]):
		# THEN
			return li[i]
		# ENDIF;
	# ENDFOR;
# END find_unique_element.


################
# Main Program #
################

n = int(input("Input the size of the array (or list): \n"))
li = [int(x) for x in input("Input the elements of the array (or list, separated by space): \n").split()]
print(find_unique_element(li))
# END.
