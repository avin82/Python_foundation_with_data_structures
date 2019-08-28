# PROGRAM multiples_of_3_in_range:

'''
Print multiples of 3 in the range a to b (both inclusive), where both a and b are given by the user.

Input Format:
a
b

Output Format:
Multiples of 3 in range a to b (both inclusive)

Sample Input 1:
3
10

Sample Output 1:
3
6
9

Sample Input 2:
8
29

Sample Output 2:
9
12
15
18
21
24
28
'''

###############################
# Print Multiples Of 3 Module #
###############################


def print_multiples_of_3_within_range():
	a = int(input("Input the starting range number to print multiples of 3 within the range (inclusive): \n"))
	b = int(input("Input the ending range number to print multiples of 3 within the range (inclusive): \n"))
	if a % 3 == 0:
	# THEN
		s = a
	elif a % 3 == 1:
	# THEN
		s = a + 2
	else:
		s = a + 1
	# ENDIF;
	for i in range(s, b + 1, 3):
	# DO
		print(i)
	# ENDFOR;
# END print_multiples_of_3_within_range.

	
################
# Main Program #
################

print_multiples_of_3_within_range()
# END.
