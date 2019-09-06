# PROGRAM swap_alternate:

'''
Given an array of length N, swap every pair of alternate elements in the array.

You don't need to print or return anything, just change in the input array itself.

Input Format:
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces

Output Format:
Elements after swapping, separated by space

Sample Input 1:
6
9 3 6 12 4 32

Sample Output 1:
3 9 12 6 32 4

Sample Input 2:
9
9 3 6 12 4 32 5 11 19

Sample Output 2:
3 9 12 6 32 4 11 5 19
'''

#########################
# Swap Alternate Module #
#########################


def swap_alternate(li):
	i = 0
	while i + 1 <= len(li) - 1:
	# DO
		li[i], li[i + 1] = li[i + 1], li[i]
		i = i + 2
	# ENDWHILE;
	for element in li:
	# DO
		print(element, end=" ")
	# ENDFOR;
# END swap_alternate.


################
# Main Program #
################

n = int(input("Input the size of the array (or list, separated by space): \n"))
li = [int(x) for x in input("Input the elements of the array (or list, separated by space): \n").split()]
swap_alternate(li)
# END.
