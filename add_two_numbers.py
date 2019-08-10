# PROGRAM add_two_numbers:

#############################
# Adding Two Numbers Module #
#############################


def add_numbers():
	num1 = int(input("Input first number: \n"))
	num2 = int(input("Input second number: \n"))
	return num1 + num2
# END add_numbers.


################
# Main Program #
################

sum = add_numbers()
print("The sum of inputted numbers is {}".format(sum))
