# PROGRAM sort_array_of_0s_and_1s:

'''
You are given an integer array A that contains only integers 0 and 1. Write a function to sort this array. Find a solution which scans the array only once. Don't use extra array.

You need to change in the given array itself. So no need to return or print anything.

Input format:
Line 1 : Integer N (Array Size)
Line 2 : Array elements (separated by space)

Output format:
Sorted array elements

Constraints :
1 <= N <= 10^6

Sample Input:
7
0 1 1 0 1 0 1

Sample Output:
0 0 0 1 1 1 1
'''

##################################
# Sort Array of 0s and 1s Module #
##################################


def sort_array_of_0s_and_1s(li):
	i, j = 0, len(li) - 1
	while i < j:
	# DO
		if li[i] != 1:
		# THEN
			i = i + 1
		# ENDIF;
		if li[j] != 0:
		# THEN
			j = j - 1
		# ENDIF;
		if li[i] == 1 and li[j] == 0 and i < j:
		# THEN
			li[i], li[j] = li[j], li[i]
			i = i + 1
			j = j - 1
		# ENDIF;
	# ENDWHILE;
	return li
# END sort_array_of_0s_and_1s.


################
# Main Program #
################

n = int(input("Input the size of the array (or list): \n"))
li = [int(x) for x in input("Input the elements of the array (or list, separated by space): \n").split()]
for element in sort_array_of_0s_and_1s(li):
# DO
	print(element, end=" ")
# ENDFOR;
# END.
