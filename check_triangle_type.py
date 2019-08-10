# PROGRAM check_triangle_type:

'''
Write a program to take 3 dimensions of a triangle input from the user. And then check if the triangle formed is equilateral, isosceles or scalene.
Print 1 if triangle is equilateral.
Print 0 if triangle is isosceles.
Print -1 if triangle is scalene.
'''

#########################
# Check Triangle Module #
#########################


def check_type_of_triangle():
	side1 = int(input("Input the length of first side of the triangle: \n"))
	side2 = int(input("Input the length of second side of the triangle: \n"))
	side3 = int(input("Input the length of third side of the triangle: \n"))
	if (side1 == side2) and (side2 == side3):
	# THEN
		print("1")
	elif (side1 == side2) or (side2 == side3) or (side3 == side1):
		print("0")
	else:
		print("-1")
	# ENDIF;
# END check_type_of_triangle.


################
# Main Program #
################

check_type_of_triangle()
print("{} represents equilateral triangle, {} represents isosceles triangle, and {} represents scalene triangle.".format(1, 0, -1))
# END.
