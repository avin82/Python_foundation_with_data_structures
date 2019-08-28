# PROGRAM reversed_triangle_pattern:

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4

   *
  **
 ***
****

Input format:
Integer N (Total no. of rows)

Output format:
Pattern in N lines

Sample Input:
5

Sample Output:
    *
   **
  ***
 ****
*****
'''

###################################
# Print Reversed Triangle Pattern #
###################################


def print_reversed_triangle_pattern():
	n = int(input("Input the number of rows to print the desired reversed triangle pattern: \n"))
	i = 1
	while i <= n:
	# DO
		spaces = 1
		while spaces <= n - i:
		# DO
			print(" ", end="")
			spaces = spaces + 1
		# ENDWHILE;
		stars = 1
		while stars <= i:
		# DO
			print("*", end="")
			stars = stars + 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_reversed_triangle_pattern.


################
# Main Program #
################

print_reversed_triangle_pattern()
# END.
