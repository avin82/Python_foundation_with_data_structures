# PROGRAM remove_consecutive_duplicates_from_string:

'''
Given a string, remove all the consecutive duplicates that are present in the given string. That means, if 'aaa' is present in the string then it should become 'a' in the output string.

Sample Input:
aabccbaa

Sample Output:
abcba
'''

####################################################
# Remove Consecutive Duplicates From String Module #
####################################################


def remove_consecutive_duplicates_from_string(str):
	duplicates_removed = ""
	i = 0
	while i < len(str):
	# DO
		j = i + 1
		while j < len(str):
		# DO
			if str[j] != str[i]:
			# THEN
				duplicates_removed = duplicates_removed + str[i]
				break
			else:
				i = j
			# ENDIF;
			j = j + 1
		# ENDWHILE;
		i = i + 1
	# ENDWHILE;
	duplicates_removed = duplicates_removed + str[i - 1]
	return duplicates_removed
# END remove_consecutive_duplicates_from_string.


################
# Main Program #
################

str = input("Input the string from which consecutive duplicates need to be removed: \n")
print(remove_consecutive_duplicates_from_string(str))
# END.
