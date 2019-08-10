# PROGRAM check_for_valid_triangle:

'''
Write a program to take 3 dimensions of a triangle input from user. And check if we can form a triangle using these 3 dimensions or not.
If triangle can be formed, print "Yes", otherwise print "No".
'''

###############################
# Check Valid Triangle Module #
###############################


def check_validity_for_triangle():
	side1 = int(input("Input the length of first side of the triangle you wish to make: \n"))
	side2 = int(input("Input the length of second side of the triangle you wish to make: \n"))
	side3 = int(input("Input the length of third side of the triangle you wish to make: \n"))
	if (side1 + side2 >= side3) or (side2 + side3 >= side1) or (side3 + side1 >= side2):
	# THEN
		print("Yes")
	else:
		print("No")
	# ENDIF;
# END check_validity_for_triangle.


################
# Main Program #
################

check_validity_for_triangle()
print("Yes - means a valid triangle can be formed from user inputted lengths of the three sides.")
print("No - means a valid triangle cannot be formed from user inputted lengths of the three sides.")
