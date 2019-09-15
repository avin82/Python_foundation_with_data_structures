# PROGRAM remove_all_char_occurrences_from_string:

'''
Given a string and a character x. Write a function to remove all occurrences of x character from the given string.

Leave the string as it is, if the given character is not present in the string.

Input format:
Line 1 : Input string
Line 2 : Character x

Sample Input:
welcome to coding ninjas
o

Sample Output:
welcme t cding ninjas
'''

##################################################
# Remove All Char Occurrences From String Module #
##################################################


def remove_char_occurrences_from_string(str, char_to_rem):
	new_str = str
	while new_str.find(char_to_rem) != -1:
	# DO
		index_of_char_to_remove = new_str.find(char_to_rem)
		new_str = new_str[:index_of_char_to_remove] + new_str[index_of_char_to_remove + 1:]
	# ENDWHILE;
	return new_str
# END remove_char_occurrences_from_string.


################
# Main Program #
################

str = input("Input the string: \n")
char_to_remove = input("Input the character to remove all it's occurrences from the string entered above: \n")
print(remove_char_occurrences_from_string(str, char_to_remove))
# END.
