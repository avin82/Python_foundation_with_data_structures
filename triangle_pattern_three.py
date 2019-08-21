# PROGRAM triangle_pattern_three:

'''
Write a program to take a number input from user. Let's say the user inputs the number 4, then the program should print the following pattern (for n = 4):

1
23
456
78910
'''

#################################
# Print Triangle Pattern Module #
#################################


def print_triangle_pattern():
	n = int(input("Input the number of rows to print the desired triangle pattern: \n"))
	i = 1
	p = 1
	while i <= n:
	# DO
		j = 1
		while j <= i:
		# DO
			print(p, end="")
			p = p + 1
			j = j + 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_triangle_pattern.


################
# Main Program #
################

print_triangle_pattern()
# END.
