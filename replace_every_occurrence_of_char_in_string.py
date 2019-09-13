# PROGRAM replace_every_occurrence_of_char_in_string:

'''
You are given a string, and are required to replace every occurrence of a given character by another character. After replacing the string should refer to the string with replaced characters.

Input Format:
Line 1: String
Line 2: char1 char2

Output Format:
Reference to the string with replaced characters

Sample Input 1:
abcda
a e

Sample Output 1:
ebcde
'''

#####################################################
# Replace Every Occurrence Of Char in String Module #
#####################################################


def replace_every_occurrence_of_char_in_string(str, char1, char2):
	new_str = ""
	for char in str:
	# DO
		if char == char1:
		# THEN
			new_str = new_str + char2
		else:
			new_str = new_str + char
		# ENDIF;
	# ENDFOR;
	return new_str
# END replace_every_occurrencee_of_char_in_string.


################
# Main Program #
################

str = input("Input a string: \n")
char1, char2 = input("Input the character to be replaced and the replacement character separated by space: \n").split()
str = replace_every_occurrence_of_char_in_string(str, char1, char2)
print(str)
# END.
