# PROGRAM print_2d_array_in_spiral_form:

'''
Given an N*M 2D array, print it in spiral form. That is, first you need to print the 1st row, then last column, then last row and then first column and so on.

Print every element only once.

Input format:
Line 1 : N and M, No. of rows & No. of columns (separated by space) followed by N*M  elements in row wise fashion.

Sample Input:
4 4 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

Sample Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
'''

########################################
# Print 2d Array In Spiral Form Module #
########################################


def print_2d_array_in_spiral_form(arr):
	row_start, row_end, col_start, col_end = 0, len(arr), 0, len(arr[0])
	row_count, col_count = row_end, col_end
	count_of_printed_elements = 0
	while count_of_printed_elements != row_count * col_count:
	# DO
		for j in range(col_start, col_end):
		# DO
			print(arr[row_start][j], end=" ")
			count_of_printed_elements = count_of_printed_elements + 1
		# ENDFOR;
		row_start = row_start + 1
		
		for i in range(row_start, row_end):
		# DO
			print(arr[i][col_end - 1], end=" ")
			count_of_printed_elements = count_of_printed_elements + 1
		# ENDFOR;
		col_end = col_end - 1
		
		for j in range(col_end - 1, col_start - 1, -1):
		# DO
			print(arr[row_end - 1][j], end=" ")
			count_of_printed_elements = count_of_printed_elements + 1
		# ENDFOR;
		row_end = row_end - 1
		
		for i in range(row_end - 1, row_start - 1, -1):
		# DO
			print(arr[i][col_start], end=" ")
			count_of_printed_elements = count_of_printed_elements + 1
		# ENDFOR;
		col_start = col_start + 1
	# ENDWHILE;
# END print_2d_array_in_spiral_form.


################
# Main Program #
################

l = [int(i) for i in input().strip().split(' ')]
m, n = l[0], l[1]
arr = [[l[(j*n)+i+2] for i in range(n)] for j in range(m)]
print_2d_array_in_spiral_form(arr)
# END.
