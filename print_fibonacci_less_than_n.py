# PROGRAM print_fibonacci_less_than_n:

##########################
# Print Fibonacci Module #
##########################


def print_fibonacci_less_than_num():
	num = int(input("Input number to print all numbers which are a part of fibonacci series and less than the entered number: \n"))
	first_num = 0
	second_num = 1
	less_than_val = True
	if num == 1:
	# THEN
		print(first_num)
	else:
		print(first_num, second_num, sep="\n")
		while less_than_val:
		# DO
			fib = first_num + second_num
			first_num = second_num
			second_num = fib
			if fib < num:
			# THEN
				print(fib)
			else:
				less_than_val = False
			# ENDIF;
		# ENDWHILE;
	# ENDIF;
# END print_fibonacci_less_than_num.


################
# Main Program #
################

print_fibonacci_less_than_num()
