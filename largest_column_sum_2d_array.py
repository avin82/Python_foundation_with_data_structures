# PROGRAM largest_column_sum_2d_array:

'''
Find the column id of the column in a 2D array with largest sum of elements.

Note: Assume that all columns are of equal length.

Input Format:
Line 1: Two integers m and n (separated by space)
Line 2: Matrix elements of each row (separated by space)

Output Format:
Column id of the column with largest sum of elements

Sample Input:
3 4
1 2 3 4 8 7 6 5 9 10 11 12

Sample Output:
3
'''

##########################################
# Find Column Id With Largest Sum Module #
##########################################


def find_largest_column_sum_2d_array(li):
	max_sum, col_id_with_max_sum = - float("inf"), - float("inf")
	for j in range(len(li[0])):
	# DO
		sum = 0
		for element in li:
		# DO
			sum = sum + element[j]
		# ENDFOR;
		if sum > max_sum:
		# THEN
			max_sum, col_id_with_max_sum = sum, j
		# ENDIF;
	# ENDFOR;
	return col_id_with_max_sum
# END find_largest_column_sum_2d_array.


################
# Main Program #
################

m, n = (int(i) for i in input().strip().split(' '))
l = [int(i) for i in input().strip().split(' ')]
arr = [[l[(j*n)+i] for i in range(n)] for j in range(m)]
print(find_largest_column_sum_2d_array(arr))
# END.
