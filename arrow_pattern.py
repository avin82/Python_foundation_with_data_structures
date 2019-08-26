# PROGRAM arrow_pattern:

'''
Print the following pattern for the given number of rows.
Assume N is always odd.

Note : There is space after every star.
Pattern for N = 7

*
 * *
   * * *
     * * * *
   * * *
 * *
*

Input format:
Integer N (Total no. of rows)

Output format:
Pattern in N lines

Sample Input:
11

Sample Output:

*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*
'''

##############################
# Print Arrow Pattern Module #
##############################


def print_arrow_pattern():
	n = int(input("Input the number of rows to print the desired arrow pattern: \n"))
	n1 = (n + 1) // 2
	n2 = n // 2
	i = 1
	while i <= n1:
	# DO
		spaces = 1
		while spaces <= i - 1:
		# DO
			print(" ", end="")
			spaces = spaces + 1
		# ENDWHILE;
		j = 1
		while j <= i:
		# DO
			print("*", end="")
			j = j + 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
	i = 1
	while i <= n2:
	# DO
		spaces = 1
		while spaces <= n2 - i:
		# DO
			print(" ", end="")
			spaces = spaces + 1
		# ENDWHILE;
		j = 1
		while j <= n2 - i + 1:
		# DO
			print("*", end="")
			j = j + 1
		# ENDWHILE;
		print()
		i = i +1
	# ENDWHILE;
# END print_arrow_pattern.


################
# Main Program #
################

print_arrow_pattern()
# END.
