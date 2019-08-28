# PROGRAM binary_pattern:

'''
Print the following pattern for the given number of rows.

Pattern for N = 4

1111
000
11
0

Input format: N (Total no. of rows)
Output format: Pattern in N lines

Sample Input:
5

Sample Output:
11111
0000
111
00
1
'''

###############################
# Print Binary Pattern Module #
###############################


def print_binary_pattern():
	n = int(input("Input the number of rows to print the desired binary pattern: \n"))
	binary_to_print = 1
	for i in range(n, 0, -1):
	# DO
		for j in range(1, i + 1, 1):
		# DO
			print(binary_to_print, end="")
		# ENDFOR;
		if binary_to_print == 1:
		# THEN
			binary_to_print = 0
		else:
			binary_to_print = 1
		# ENDIF;
		print()
	# ENDFOR;
# END print_binary_pattern.


################
# Main Program #
################

print_binary_pattern()
# END.
