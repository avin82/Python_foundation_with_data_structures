# PROGRAM largest_row_or_col_sum_2d_array:

'''
Given an NxM 2D array, you need to find out which row or column has largest sum (sum of its elements) overall amongst all rows and columns.

Input Format:
Line 1 : 2 integers N and M respectively, separated by space
Line 2: Single line having N*M elements entered in row wise manner, each separated by space.

Output Format:
If row sum is maximum then - "row" row_num max_sum
If column sum is maximum then - "column" col_num max_sum

Note : If there are more than one rows/columns with maximum sum consider the row/column that comes first. And if ith row and jth column has same sum (which is largest), consider the ith row as answer.

Sample Input 1:
2 2
1 1 1 1

Sample Output 1:
row 0 2

Sample Input 2:
3 3
3 6 9 1 4 7 2 8 9

Sample Output 2:
column 2 25
'''

######################################
# Find Largest Row Or Col Sum Module #
######################################


def find_largest_row_or_col_sum(arr):
	max_sum, max_entity, row_id, col_id = - float("inf"), "", - float("inf"), - float("inf")
	for i in range(len(arr)):
	# DO
		sum = 0
		for j in range(len(arr[i])):
		# DO
			sum = sum + arr[i][j]
		# ENDFOR;
		if sum > max_sum:
		# THEN
			max_sum, max_entity, row_id = sum, "row", i
		# ENDIF;
	# ENDFOR;
	for j in range(len(arr[0])):
	# DO
		sum = 0
		for i in range(len(arr)):
		# DO
			sum = sum + arr[i][j]
		# ENDFOR;
		if sum > max_sum:
		# THEN
			max_sum, max_entity, col_id = sum, "column", j
		# ENDIF;
	# ENDFOR;
	if max_entity == "row":
	# THEN
		return [max_entity, row_id, max_sum]
	else:
		return [max_entity, col_id, max_sum]
	# ENDIF;
# END find_largest_row_or_col_sum.


################
# Main Program #
################

m, n= (int(i) for i in input().strip().split(' '))
l = [int(i) for i in input().strip().split(' ')]
arr = [[l[(j*n)+i] for i in range(n)] for j in range(m)]
l = find_largest_row_or_col_sum(arr)
print(*l)
# END.
