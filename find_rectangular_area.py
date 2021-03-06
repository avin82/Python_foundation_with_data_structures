# PROGRAM find_rectangular_area:

'''
You are given a rectangle in a plane. The corner coordinates of this rectangle is provided to you. You have to print the amount of area of the plane covered by this rectangles.
The end coordinates are provided as four integral values: x1, y1, x2, y2. It is given that x1 < x2 and y1 < y2.

Input format:
The first line of input contains an integer x1 (1 <= x1 <= 10)
The second line of input contains an integer y1 (1 <= y1 <= 10)
The third line of input contains an integer x2 (1 <= x2 <= 10)
The fourth line of input contains an integer y2 (1 <= y2 <= 10)

Constraints:
Time Limit: 1 second

Output format:
The first and only line of output contains the result.

Sample Input:
1
1
3
3

Sample Output:
4
'''

################################
# Find Rectangular Area Module #
################################


def find_rectangular_area():
	x1 = int(input("Input the x coordinate value of the first corner of the rectangle: \n"))
	y1 = int(input("Input the y coordinate value of the first corner of the rectangle: \n"))
	x2 = int(input("Input the x coordinate value of the second corner of the rectangle: \n"))
	y2 = int(input("Input the y coordinate value of the second corner of the rectangle: \n"))
	return (x2 - x1) * (y2 - y1)


################
# Main Program #
################

print(find_rectangular_area())
# END.
