# PROGRAM find_sum_of_unique_nums_in_a_list:

'''
Given a list, find sum of all the unique numbers in that list.

Input Format:
Line 1 : An Integer N i.e. size of array or list
Line 2 : N integers which are elements of the array or list, separated by spaces

Output Format:
Sum of unique elements in the list
'''

######################################
# Find Sum Of Unique Elements Module #
######################################


def sum_of_unique_elements(li):
	s = set()
	[s.add(element) for element in li]
	sum = 0
	for element in s:
	# DO
		sum = sum + element
	# ENDFOR;
	return sum
# END sum_of_unique_elements.


################
# Main Program #
################

n = int(input("Input the size of the array or list: \n"))
li = [int(x) for x in input("Input the elements of the array or list separated by spaces: \n").split()]
print(sum_of_unique_elements(li))
# END.
