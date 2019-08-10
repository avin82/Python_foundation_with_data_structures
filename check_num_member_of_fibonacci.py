# PROGRAM check_num_member_of_fibonacci:

'''
Wite a program to take a number N input from user and check if that number is member of fibonacci series or not.
Print "Yes" or "No" accordingly.
'''

####################################
# Check Number As Fibonacci Module #
####################################


def check_is_num_member_of_fibonacci():
	num = int(input("Input number to check whether the entered number is a member of fibonacci series or not: \n"))
	first_num = 0
	second_num = 1
	if (num == first_num) or (num == second_num):
	# THEN
		return True
	else:
		while first_num + second_num <= num:
		# DO
			fib = first_num + second_num
			if num == fib:
			# THEN
				return True
			# ENDIF;
			first_num = second_num
			second_num = fib
		# ENDWHILE;
	# ENDIF;
	return False
# END check_is_num_member_of_fibonacci.


################
# Main Program #
################

if check_is_num_member_of_fibonacci():
# THEN
	print("Yes")
else:
	print("No")
# ENDIF;
# END.
