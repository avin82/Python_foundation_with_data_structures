# PRORGAM isosceles_traingle_pattern:

'''
Print the following pattern for the given N number of rows.

Pattern for N = 4

   1
  121
 12321
1234321

Input format:
Integer N (Total no. of rows)

Output format:
Pattern in N lines

Sample Input:
5

Sample Output:
    1
   121
  12321
 1234321
123454321
'''

####################################
# Print Isosceles Triangle Pattern #
####################################


def print_isosceles_triangle_pattern():
	n = int(input("Input the number of rows to print the desired isosceles triangle pattern: \n"))
	i = 1
	while i <= n:
	# DO
		spaces = 1
		# spaces
		while spaces <= n - i:
		# DO
			print(" ", end="")
			spaces = spaces + 1
		# ENDWHILE;
		p = 1
		j = 1
		# increasing sequence
		while j <= i:
		# DO
			print(p, end="")
			j = j + 1
			p = p + 1
		# ENDWHILE;
		# decreasing sequence
		p = i - 1
		while p >= 1:
		# DO
			print(p, end="")
			p = p - 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_isosceles_triangle_pattern.


################
# Main Program #
################

print_isosceles_triangle_pattern()
# END.
