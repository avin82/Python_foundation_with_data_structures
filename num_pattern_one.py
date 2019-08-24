# PROGRAM num_pattern_one:

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4

1
11
111
1111

Input format:
Integer N (Total no. of rows)

Output format:
Pattern in N lines

Sample Input:
5

Sample Output:
1
11
111
1111
11111
'''

###############################
# Print Number Pattern Module #
###############################


def print_num_pattern():
	n = int(input("Input the number of rows to print the desired number pattern"))
	i = 1
	while i <= n:
	# DO
		j = 1
		while j <= i:
		# DO
			print(1, end="")
			j = j + 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_num_pattern.


################
# Main Program #
################

print_num_pattern()
# END.
