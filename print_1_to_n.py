# PROGRAM print_1_to_n:

################
# Print Module #
################


def print_till_num():
	num = int(input("Input number till which you want to print all numbers starting from 1: \n"))
	count = 1
	while count <= num:
	# DO
		print(count)
		count = count + 1
	# ENDWHILE;
# END print_till_num.


################
# Main Program #
################

print_till_num()
