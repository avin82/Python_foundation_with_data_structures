# PROGRAM pyramid_num_pattern:

'''
Print the following pattern for the given number of rows.

Pattern for N = 4

   1
  212
 32123
4321234

Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input:
5

Sample Output:
    1
   212
  32123
 4321234
543212345
'''

########################################
# Print Pyramind Number Pattern Module #
########################################


def print_pyramid_num_pattern():
	n = int(input("Input the number of rows to print the desired pyramid number pattern: \n"))
	i = 1
	while i <= n:
	# DO
		spaces = 1
		while spaces <= n - i:
		# DO
			print(" ", end="")
			spaces = spaces + 1
		# ENDWHILE;
		j = i
		while j >= 1:
		# DO
			print(j, end="")
			j = j - 1
		# ENDWHILE;
		k = 2
		while k <= i:
		# DO
			print(k, end="")
			k = k + 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_pyramid_num_pattern.


################
# Main Program #
################

print_pyramid_num_pattern()
# END.
