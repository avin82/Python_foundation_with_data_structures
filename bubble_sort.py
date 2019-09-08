# PROGRAM bubble_sort:

'''
Given a random integer array. Sort this array using bubble sort.

Change in the input array itself. You don't need to return or print elements.
Input format:
Line 1 : Integer N, Array Size
Line 2 : Array elements (separated by space)

Constraints :
1 <= N <= 10^3

Sample Input 1:
7
2 13 4 1 3 6 28

Sample Output 1:
1 2 3 4 6 13 28

Sample Input 2:
5
9 3 6 2 0

Sample Output 2:
0 2 3 6 9
'''

######################
# Bubble Sort Module #
######################


def bubble_sort(li):
	for i in range(len(li)):
	# DO
		for j in range(len(li) - i - 1):
		# DO
			if li[j] > li[j + 1]:
			# THEN
				li[j], li[j + 1] = li[j + 1], li[j]
			# ENDIF;
		# ENDFOR;
	# ENDFOR;
	return li
# END bubble_sort.


################
# Main Program #
################

n = int(input("Input the size of array (or list): \n"))
li = [int(x) for x in input("Input the elements of array (or list, separated by space): \n").split()]
for element in bubble_sort(li):
# DO
	print(element, end=" ")
# ENDFOR;
# END.
