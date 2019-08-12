# PROGRAM is_num_palindrome:

'''
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.

Note: Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

Sample Input 1:
121

Sample Output 1:
true

Sample Input 2:
1032

Sample Output 2:
false
'''

###########################
# Check Palindrome Module #
###########################


def check_palindrome():
	num = int(input("Input number to be checked for being palindrome or not: \n"))
	original_num = num
	rev = 0
	while num != 0:
	# DO
		rev = rev * 10 + num % 10
		num = num // 10
	# ENDWHILE;
	return rev == original_num
# END check_palindrome.


################
# Main Program #
################

if check_palindrome():
#THEN
	print("true")
else:
	print("false")
# ENDIF;
#END.

