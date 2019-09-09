# PROGRAM merge_sorted_arrays:

'''
Given two sorted arrays of Size M and N respectively, merge them into a third array such that the third array is also sorted.

Input Format:
Line 1 : Size of first array i.e. M
Line 2 : M elements of first array separated by space
Line 3 : Size of second array i.e. N
Line 2 : N elements of second array separated by space

Output Format:
M + N integers i.e. elements of third sorted array separated by spaces

Constraints :
1 <= M, N <= 10^6

Sample Input:
5
1 3 4 7 11
4
2 4 6 13

Sample Output:
1 2 3 4 4 6 7 11 13
'''

##################################
# Merge Sorted Arrays Module #
##################################


def merge_sorted_arrays(li_m, li_n):
	i, j, li_s = 0, 0, []
	while i < len(li_m) and j < len(li_n):
	# DO
		if li_m[i] <= li_n[j]:
		# THEN
			li_s.append(li_m[i])
			i = i + 1
		else:
			li_s.append(li_n[j])
			j = j + 1
		# ENDIF;
	# ENDWHILE;

	if i == len(li_m):
	# THEN
		for element in li_n[j:]:
		# DO
			li_s.append(element)
		# ENDFOR;
	elif j == len(li_n):
	# THEN
		for element in li_m[i:]:
		# DO
			li_s.append(element)
		# ENDFOR;
	# ENDIF;
	return li_s
# END merge_two_sorted_arrays.


################
# Main Program #
################

m = int(input("Input the size of first array (or list): \n"))
li_m = [int(x) for x in input("Input the elements of first sorted array (or list, separated by space): \n").split()]
n = int(input("Input the size of second array (or list): \n"))
li_n = [int(x) for x in input("input the elements of second sorted array (or list, separated by space): \n").split()]
for element in merge_sorted_arrays(li_m, li_n):
# DO
	print(element, end=" ")
# ENDFOR;
# END.
