# PROGRAM rectangular_numbers_pattern:

'''
Print the following pattern for the given number of rows.

Pattern for N = 4

4444444
4333334
4322234
4321234
4322234
4333334
4444444

Input format : N (Total no. of rows)
Output format : Pattern in N lines

Sample Input:
3

Sample Output:
33333
32223
32123
32223
33333
'''

###########################################
# Print Rectangular Number Pattern Module #
###########################################


def print_rectangular_numbers_pattern():
	n = int(input("Input number of rows to print the desired rectangular number pattern: \n"))
	for i in range(1, n + 1):
	# DO
		temp = n
		for j in range(1, i):
		# DO
			print(temp, end="")
			temp = temp - 1
		# ENDFOR;
		for j in range(1, (2 * n) - (2 * i) + 2):
		# DO
			print(n - i + 1, end="")
		# ENDFOR;
		for j in range(1, i):
		# DO
			temp = temp + 1
			print(temp, end="")
		# ENDFOR;
		print()
	# ENDFOR;
	
	for i in range(n - 1, 0, -1):
	# DO
		temp = n
		for j in range(1, i):
		# DO
			print(temp, end="")
			temp = temp - 1
		# ENDFOR;
		for j in range(1, (2 * n) - (2 * i) + 2):
		# DO
			print(n - i + 1, end="")
		# ENDFOR;
		for j in range(1, i):
		# DO
			temp = temp + 1
			print(temp, end="")
		# ENDFOR;
		print()
	# ENDFOR;
# END print_rectangular_numbers_pattern.


################
# Main Program #
################

print_rectangular_numbers_pattern()
# END.
