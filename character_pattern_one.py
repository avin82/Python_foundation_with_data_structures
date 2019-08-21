# PROGRAM character_pattern_one:

'''
Write a program to take a number input from user. Let's say the user inputs the number 4, then the program should print the following pattern (for n = 4):

ABCD
ABCD
ABCD
ABCD
'''

#####################################
# Character Pattern Printing Module #
#####################################


def print_character_pattern():
	n = int(input("Input the number of rows which is equal to the number of columns to print the desired square character pattern: \n"))
	i = 1
	while i <= n:
	# DO
		j = 1
		while j <= n:
		# DO
			char_to_print = chr(ord('A') + j - 1)
			print(char_to_print, end="")
			j = j + 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_character_pattern.


################
# Main Program #
################

print_character_pattern()
# END.
