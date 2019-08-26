# PROGRAM inverted_triangle_pattern:

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4

****
***
**
*

Input format:
Integer N (Total no. of rows)

Output format:
Pattern in N lines

Sample Input:
5

Sample Output:
*****
****
***
**
*
'''

###################################
# Print Inverted Triangle Pattern #
###################################


def print_inverted_triangle_pattern():
	n = int(input("Input the number of rows to print the desired inverted triangle pattern: \n"))
	i = 1
	while i <= n:
	# DO
		j = 1
		while j <= n - i + 1:
		# DO
			print("*", end="")
			j = j + 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_inverted_triangle_pattern.


################
# Main Program #
################

print_inverted_triangle_pattern()
# END.
		
