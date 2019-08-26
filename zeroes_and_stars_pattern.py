# PROGRAM zeroes_and_stars_pattern:

'''
Print the following pattern

Pattern for N = 4

*000*000*
0*00*00*0
00*0*0*00
000***000

Input Format:
N (Total no. of rows)

Output Format:
Pattern in N lines

Sample Input 1:
3

Sample Output 1:
*00*00*
0*0*0*0
00***00

Sample Input 2:
5

Sample Output 2:
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
'''

#########################################
# Print Zeroes and Stars Pattern Module #
#########################################


def print_zeroes_and_stars_pattern():
	n = int(input("Input the number of rows to print the desired zeroes and stars pattern: \n"))
	i = 1
	while i <= n:
	# DO
		j = 1
		while j <= n:
		# DO
			if j == i:
			# THEN
				print("*", end="")
			else:
				print(0, end="")
			# ENDIF;
			j = j + 1
		# ENDWHILE;
		print("*", end="")
		k = 1
		while k <= n:
		# DO
			if k != n - i + 1:
			# THEN
				print(0, end="")
			else:
				print("*", end="")
			# ENDIF;
			k = k + 1
		# ENDWHILE;
		print()
		i = i + 1
	# ENDWHILE;
# END print_zeroes_and_stars_pattern.


################
# Main Program #
################

print_zeroes_and_stars_pattern()
# END.
