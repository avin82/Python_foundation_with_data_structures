# PROGRAM diamond_of_stars:

'''
Print the following pattern for the given number of rows.

Assume, N is always odd.

Pattern for N = 7

   *
  ***
 *****
*******
 *****
  ***
   *

Input Format:
N (Total no. of rows and can only be odd)

Output Format:
Pattern in N lines

Sample Input:
5

Sample Output:
  *
 ***
*****
 ***
  *
'''

#################################
# Print Diamond Of Stars Module #
#################################


def print_diamond_of_stars():
	n = int(input("Input the number of rows (which is an odd number) to print the diamond of stars: \n"))
	x = (n + 1) // 2
	y = n // 2
	for i in range(1, x + 1, 1):
	# DO
		spaces = x - i
		for s in range(1, spaces + 1, 1):
		# DO
			print(" ", end="")
		# ENDFOR;
		for j in range(1, 2 * i, 1):
		# DO
			print("*", end="")
		# ENDFOR;
		print()
	# ENDFOR;
	for i in range(y, 0, -1):
	# DO
		spaces = y - i + 1
		for s in range(1, spaces + 1, 1):
		# DO
			print(" ", end="")
		# ENDFOR;
		for j in range(1, 2 * i, 1):
		# DO
			print("*", end="")
		# ENDFOR;
		print()
	# ENDFOR;
# END print_diamond_of_stars.


################
# Main Program #
################

print_diamond_of_stars()
# END.
