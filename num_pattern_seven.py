# PROGRAM num_pattern_seven:

'''
Print the following pattern for the given number of rows.

Pattern for N = 5

1    2   3    4   5
11   12  13   14  15
21   22  23   24  25
16   17  18   19  20
6    7    8   9   10

Input format : N (Total no. of rows)
Output format : Pattern in N lines

Sample Input:
4

Sample Output:
1  2  3  4
9 10 11 12
13 14 15 16
5  6  7  8
'''

###############################
# Print Number Pattern Module #
###############################

def print_number_pattern():
	n = int(input("Input number of rows to print the number pattern: \n"))
	start_val = 1
	for i in range(1, n + 1):
	# DO
		for j in range(start_val, start_val + n):
		# DO
			print(j, end=" ")
		# ENDFOR;
		print()
		if (i == (n + 1) // 2):
		# THEN
			if n % 2 != 0:
			# THEN
				start_val = n * (n - 2) + 1
			else:
				start_val = n * (n - 1) + 1
			# ENDIF;
		elif i > (n + 1) // 2:
		# THEN
			start_val = start_val - 2 * n
		else:
			start_val = start_val + 2 * n
		# ENDIF;
	# ENDFOR;
# END print_number_pattern.


################
# Main Program #
################

print_number_pattern()
# END.
