# PROGRAM is_num_armstrong:

'''
Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.

An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
For example,

371, as 3**3 + 7**3 + 1**3 = 371
1634, as 1**4 + 6**4 + 3**4 + 4**4 = 1634

Input Format:
Integer n

Output Format:
true or false

Sample Input 1:
1

Sample Output 1:
true

Sample Input 2:
103

Sample Output 2:
false
'''

##########################
# Check Armstrong Module #
##########################


def check_armstrong():
	n = int(input("Input number to be checked for armstrong: \n"))
	num_digits = 0
	dividend = n
	while dividend != 0:
	# DO
		dividend = dividend // 10
		num_digits = num_digits + 1
	# ENDWHILE;
	armstrong = 0
	count = 0
	dividend = n
	while count <= num_digits:
	# DO
		div_10_remainder = dividend % 10
		armstrong = armstrong + div_10_remainder ** num_digits
		count = count + 1
		dividend = dividend // 10
	# ENDWHILE;
	return n == armstrong
# END check_armstrong.


################
# Main Program #
################

if check_armstrong():
# THEN
	print("true")
else:
	print("false")
# ENDIF;
# END.

