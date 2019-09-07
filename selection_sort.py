# PROGRAM selection_sort:

#########################
# Selection Sort Module #
#########################


def selection_sort(li):
	for selection in range(len(li) - 1):
	# DO
		for comparator in range(selection + 1, len(li)):
		# DO
			if li[comparator] < li[selection]:
			# THEN
				li[selection], li[comparator] = li[comparator], li[selection]
			# ENDIF;
		# ENDFOR;
	# ENDFOR;
	return li
# END selection_sort.


################
# Main Program #
################

n = int(input("Input the size of array (or list): \n"))
li = [int(x) for x in input("Input the elements of the array (or list, separated by space): \n").split()]
for element in selection_sort(li):
# DO	
	print(element, end=" ")
# ENDFOR;
print()
# END.
