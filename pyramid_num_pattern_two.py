# PROGRAM pyramid_num_pattern_two:

'''
Print the following pattern for a given n.

For eg. N = 6

123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456

Sample Input 1:
4

Sample Output 1:
1234
 234
  34
   4
  34
 234
1234
'''

#######################################
# Print Pyramid Number Pattern Module #
#######################################


def print_pyramid_num_pattern():
	n = int(input("Input the number of rows to print the desired pyramid number pattern: \n"))
	for i in range(1, n + 1, 1):
	# DO
		spaces = i - 1
		for j in range(1, spaces + 1, 1):
		# DO
			print(" ", end="")
		# ENDFOR;
		for k in range(i, n + 1, 1):
		# DO
			print(k, end="")
		# ENDFOR;
		print()
	# ENDFOR;
	for i in range(n - 1, 0, -1):
	# DO
		spaces = i - 1
		for j in range(1, spaces + 1, 1):
		# DO
			print(" ", end="")
		# ENDFOR;
		for k in range(i, n + 1, 1):
		# DO
			print(k, end="")
		# ENDFOR;
		print()
	# ENDFOR;
# END print_pyramid_num_pattern.


################
# Main Program #
################

print_pyramid_num_pattern()
# END.
