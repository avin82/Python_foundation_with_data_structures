# PROGRAM find_product_1_to_n:

#######################
# Find Product Module #
#######################


def find_product_till_num():
	num = int(input("Input the number to calculate the product of series starting from 1 till the entered number: \n"))
	product = num
	while (num - 1) != 0:
	# DO
		product = product * (num - 1)
		num = num - 1
	# ENDWHILE;
	return product
# END find_product_till_num.


################
# Main Program #
################

print(find_product_till_num())
