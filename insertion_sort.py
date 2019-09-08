# PROGRAM insertion_sort:

'''
Given a random integer array. Sort this array using insertion sort.

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

#########################
# Insertion Sort Module #
#########################


def insertion_sort(li):
	for i in range(1, len(li)):
	# DO
		key_to_insert = li[i]
		j = i - 1
		while j >= 0 and key_to_insert < li[j]:
		# DO
			li[j + 1] = li[j]
			j = j - 1
		# ENDWHILE;
		li[j + 1] = key_to_insert
	# ENDFOR;
	return li
# END insertion_sort.


################
# Main Program #
################
		
n = int(input("Input the size of array (or list): \n"))
li = [int(x) for x in input("Input the elements of the array (or list, separated by space): \n").split()]
for element in insertion_sort(li):
# DO
	print(element, end=" ")
# ENDFOR;
# END.
			
