# PROGRAM check_num_positive_negative_or_zero:

'''
Write a program to take a number input from user and check if that number is positive, negative or Zero.
Print 1, if number is positive.
Print -1, if number is negative.
Print 0, if number is 0.
'''

#######################
# Check Number Module #
#######################


def check_number():
	num = int(input("Input the number you want to be checked for positive, negative or zero: \n"))
	if num > 0:
	# Then
		return 1
	elif num < 0:
	# THEN
		return -1
	else:
		return 0
	# ENDIF;
# END check_number.


################
# Main Program #
################

print(check_number())
print("1 stands for positive, -1 stands for negative and 0 stands for zero.\n")
