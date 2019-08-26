# PROGRAM num_pattern_five:

'''
Print the following pattern for n number of rows.

For eg. N = 5

1        1
12      21
123    321
1234  4321
1234554321

Sample Input 1:
4

Sample Output 1:
1      1
12    21
123  321
12344321
'''

###############################
# Print Number Pattern Module #
###############################


def print_num_pattern():
	n = int(input("Input the number of rows to print the desired number pattern: \n"))
	i = 1
	while i <= n:
	# DO
		j = 1
		while j <= i:
		# DO
			print(j, end="")
			j = j + 1
		# ENDWHILE;
		spaces = 1
		while spaces <= n - i:
		# DO
			print(" ", end="")
			spaces = spaces + 1
		# ENDWHILE;
		spaces = 1
		while spaces <= n - i:
		# DO
			print(" ", end="")
			spaces = spaces + 1
		# ENDWHILE;
		k = i
		while k >= 1:
		# DO
			print(k, end="")
			k = k - 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_num_pattern.


################
# Main Program #
################

print_num_pattern()
# END.
