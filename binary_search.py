# PROGRAM binary_search:

'''
Given a sorted integer array (in ascending order) and an element x. You need to search this element x in the given input array using binary search. Return the index of element in the input.

Indexing starts from 0.
Return -1 if x is not present in the input array.
Input format:
Line 1 : Integer N, Array Size
Line 2 : Array elements (separated by space)
Line 3 : Element to be searched (i.e. x)

Output format:
Index	

Constraints :
1 <= N <= 10^6

Sample Input 1:
7
1 3 7 9 11 12 45
3

Sample Output 1:
1

Sample Input 2:
7
1 2 3 4 5 6 7
9

Sample Output 2:
-1
'''

########################
# Binary Search Module #
########################


def binary_search(li, element):
	start, end = 0, len(li) - 1
	while start <= end:
	# DO
		mid = (start + end) // 2
		if element > li[mid]:
		# THEN
			start = mid + 1
		elif element < li[mid]:
		# THEN
			end = mid - 1
		else:
			return mid
		# ENDIF;
	# ENDWHILE;
	return -1
# END binary_search.


################
# Main Program #
################

n = int(input("Input the size of the array (or list): \n"))
li = [int(x) for x in input("Input the elements of the array (or list, separated by space): \n").split()]
x = int(input("Input the element to be searched in the array (or list): \n"))
print(binary_search(li, x))
# END.
