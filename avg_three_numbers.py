# PROGRAM avg_three_numbers:

##########################
# Finding Average Module #
##########################


def find_avg():
	num1 = int(input("Input first number: \n"))
	num2 = int(input("Input second number: \n"))
	num3 = int(input("Input third  number: \n"))
	return (num1 + num2 + num3) / 3


################
# Main Program #
################

avg = find_avg()
print("Average of user inputted numbers is {}".format(avg))
