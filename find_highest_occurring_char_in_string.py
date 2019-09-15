# PROGRAM find_highest_occurring_char_in_string:

'''
Given a string, find and return the highest occurring character present in the given string.

If there are 2 characters in the input string with same frequency, return the character which comes first.

Note : Assume all the characters in the given string are lowercase.

Sample Input 1:
abdefgbabfba

Sample Output 1:
b

Sample Input 2:
xy

Sample Output 2:
x
'''

################################################
# Find Highest Occurring Char In String Module #
################################################


def find_highest_occurring_char_in_string(str):
	count_of_highest_occurrence, char_with_highest_occurrence, already_counted_chars = - float("inf"), "", []
	for i in range(len(str)):
	# DO
		if str[i] in already_counted_chars:
		# THEN
			continue
		else:
			count_of_char = 1
			j = i + 1
			for j in range(len(str)):
			# DO
				if str[j] == str[i]:
				# THEN
					count_of_char = count_of_char + 1
				# ENDIF;
			# ENDFOR;
			if count_of_char > count_of_highest_occurrence:
			# THEN
				count_of_highest_occurrence, char_with_highest_occurrence = count_of_char, str[i]
			# ENDIF;
			already_counted_chars.append(str[i])
		# ENDIF;
	# ENDFOR;
	return char_with_highest_occurrence


################
# Main Program #
################

str = input("Input the string to find the highest occurring character in it: \n")
print(find_highest_occurring_char_in_string(str))
# END.
