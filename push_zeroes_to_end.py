# PROGRAM push_zeroes_to_end:

'''
Given a random integer array, push all the zeros that are present to end of the array. The respective order of other elements should remain same.

Change in the input array itself. You don't need to return or print elements. Don't use extra array.

Note : You need to do this in one scan of array only.
Input format:
Line 1 : Integer N, Array Size
Line 2 : Array elements (separated by space)

Output Format:
Array elements (separated by space)

Constraints :
1 <= N <= 10^6

Sample Input 1:
7
2 0 4 1 3 0 28

Sample Output 1:
2 4 1 3 28 0 0

Sample Input 2:
5
0 3 0 2 0

Sample Output 2:
3 2 0 0 0
'''

#############################
# Push Zeroes To End Module #
#############################


def push_zeroes_to_end(li):
	non_zero_pos = 0
	for iter_var in range(len(li)):
	# DO
		if li[iter_var] == 0:
		# THEN
			continue
		# ENDIF;
		li[non_zero_pos] = li[iter_var]
		non_zero_pos = non_zero_pos + 1
	# ENDFOR;
	for leftover_zero_pos in range(non_zero_pos, len(li)):
	# DO
		li[leftover_zero_pos] = 0
	# ENDFOR;
	return li
# END push_zeroes_to_end.


################
# Main Program #
################

n = int(input("Input the size of array (or list): \n"))
li = [int(x) for x in input("Input the elements of array (or list, separated by space): \n").split()]
for element in push_zeroes_to_end(li):
# DO
	print(element, end=" ")
# ENDFOR;
# END.
