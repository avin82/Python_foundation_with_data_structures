# PROGRAM num_pattern_four:

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4

1234
123
12
1

Input format:
Integer N (Total no. of rows)

Output format:
Pattern in N lines

Sample Input:
5

Sample Output:
12345
1234
123
12
1
'''

###############################
# Print Number Pattern Module #
###############################


def print_num_pattern():
	n = int(input("Input the number of rows to print the desired number pattern: \n"))
	p = n
	i = 1
	while i <= n:
	# DO
		j = 1
		while j <= p:
		# DO
			print(j, end="")
			j = j + 1
		# ENDWHILE;
		p = p - 1
		print()
		i = i + 1
	# ENDWHILE;
# END print_num_pattern.


################
# Main Program #
################

print_num_pattern()
# END.
