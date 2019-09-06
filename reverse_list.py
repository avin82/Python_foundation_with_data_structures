# PROGRAM reverse_list:

'''
Write a program to reverse the elements of a list.

Sample Input:
2 3 5 6 7 9

Sample Output:
9 7 6 5 3 2
'''

#######################
# Reverse List Module #
#######################


def reverse_list(li):
	for i in range(len(li) // 2):
	# DO
		li[i], li[-i - 1] = li[-i - 1], li[i]
	# ENDFOR;
	for element in li:
	# DO
		print(element, end=" ")
	# ENDFOR;
# END reverse_list.


################
# Main Program #
################

li = [int(x) for x in input("Input the elements of the list (separated by list) which need to be reversed: \n").split()]
reverse_list(li)
# END.
