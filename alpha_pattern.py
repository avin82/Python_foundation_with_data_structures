# PROGRAM alpha_pattern:

'''
Print the following pattern for the given N number of rows.

Pattern for N = 3

A
BB
CCC

Input format:
Integer N (Total no. of rows)

Output format:
Pattern in N lines

Sample Input:
7

Sample Output:
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
'''

#################################
# Print Alphabet Pattern Module #
#################################


def print_alpha_pattern():
	n = int(input("Input the number of rows to print the desired alphabet pattern: \n"))
	i = 1
	while i <= n:
	# DO
		char_to_print = chr(ord('A') + i - 1)
		j = 1
		while j <= i:
		# DO
			print(char_to_print, end="")
			j = j + 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_alpha_pattern.


################
# Main Program #
################

print_alpha_pattern()
# END.
