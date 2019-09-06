# PROGRAM array_intersection:

'''
Given two random integer arrays of size m and n, print their intersection. That is, print all the elements that are present in both the given arrays.
Input arrays can contain duplicate elements.

Note : Order of elements are not important

Input format:
Line 1 : Array 1 Size
Line 2 : Array 1 elements (separated by space)
Line 3 : Array 2 Size
Line 4 : Array 2 elements (separated by space)

Output format:
Print intersection elements in different lines

Constraints :
1 <= m, n <= 10^3

Sample Input 1:
6
2 6 8 5 4 3
4
2 3 4 7

Sample Output 1:
2
4
3

Sample Input 2:
4
2 6 1 2
5
1 2 3 4 2

Sample Output 2:
2
2
1
'''

##################################
# Find Array Intersection Module #
##################################


def find_array_intersection(li_m, li_n):
	i = 0
	while i < len(li_m) and len(li_n) > 0:
	# DO
		if li_m[i] in li_n:
		# THEN
			print(li_m[i])
			li_n.remove(li_m[i])
		# ENDIF;
		i = i + 1
	# ENDWHILE;
# END find_array_intersection.


################
# Main Program #
################

m = int(input("Input the size of the first array (or list): \n"))
li_m = [int(x) for x in input("Input the elements of the first array (or list, separated by space): \n").split()]
n = int(input("Input the size of the second array (or list): \n"))
li_n = [int(x) for x in input("Input the elements of the second array (or list, separated by space): \n").split()]
find_array_intersection(li_m, li_n)
# END.
