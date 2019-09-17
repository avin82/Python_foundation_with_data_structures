# PROGRAM print_2d_array_in_sine_wave_order:

'''
Given a two dimensional n*m array, print the array in a sine wave order. i.e. print the first column top to bottom, next column bottom to top and so on.

Note : Print the elements separated by space.

Input format:
n, m, array elements (separated by space)

Sample Input:
3 4 1 2 3 4 5 6 7 8 9 10 11 12

Sample Output:
1 5 9 10 6 2 3 7 11 12 8 4
'''

############################################
# Print 2d Array In Sine Wave Order Module #
############################################


def print_2d_array_in_sine_wave_order(arr):
	for j in range(len(arr[0])):
	# DO
		if j % 2 == 0:
		# THEN
			for i in range(len(arr)):
			# DO
				print(arr[i][j], end=" ")
			# ENDFOR;
		else:
			for i in range(len(arr) - 1, -1, -1):
			# DO
				print(arr[i][j], end=" ")
			# ENDFOR;
		# ENDIF;
	# ENDFOR;
# END print_2d_array_in_sine_wave_order.


################
# Main Program #
################

l = [int(i) for i in input().strip().split(" ")]
m, n = l[0], l[1]
arr = [[l[(j*n)+i+2] for i in range(n)] for j in range(m)]
print_2d_array_in_sine_wave_order(arr)
# END.
