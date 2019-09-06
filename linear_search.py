# PROGRAM linear_search:

'''
Perform linear search to find an element in a list and return the index of the found element. If the element does not exist in the list then return -1.

Sample Input 1:
2 5 7 9 11 13 15
9

Sample Output 1:
3

Sample Input 1:
23 45 67 89 97
25

Sample Output 2:
-1
'''


########################
# Linear Search Module #
########################


def linear_search(li, element):
	for i in range(len(li)):
	# DO
		if li[i] == element:
		# THEN
			return i
		# ENDIF;
	# ENDFOR;
	return -1
# END linear_search.


################
# Main Program #
################
	
li = [int(x) for x in input("Input the elements of the list separated by space: \n").split()]
n = int(input("Input the element to be searched for in the given list: \n"))
print(linear_search(li, n))
# END.
