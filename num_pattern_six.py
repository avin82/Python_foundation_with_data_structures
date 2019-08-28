# PROGRAM num_pattern_six:

'''
Print the following pattern for n number of rows.

For e.g. N = 4

   1
  232
 34543
4567654

Input Format:
Integer N (Total no. of rows)

Output Format:
Pattern in N lines

Sample Input:
5

Sample Output:
    1
   232
  34543
 4567654
567898765
'''

###############################
# Print Number Pattern Module #
###############################


def print_num_pattern():
	n = int(input("Input the number of rows to print the desired number pattern: \n"))
	for i in range(1, n + 1, 1):
	# DO
		for s in range(n - i):
		# DO
			print(" ", end="")
		# ENDFOR;
		for j in range(i, 2 * i, 1):
		# DO
			print(j, end="")
		# ENDFOR;
		for k in range(2 * i - 2, i - 1, -1):
		# DO
			print(k, end="")
		# ENDFOR;
		print()
# END print_num_pattern.


################
# Main Program #
################

print_num_pattern()
# END.
