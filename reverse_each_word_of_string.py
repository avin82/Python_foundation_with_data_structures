# PROGRAM reverse_each_word_of_string:

'''
Given a string S, reverse each word of a string individually. For eg. if a string is "abc def", reversed string should be "cba fed".

Input Format:
String S

Output Format:
Updated string

Constraints :
1 <= Length of S <= 1000

Sample Input:
Welcome to Coding Ninjas

Sample Output:
emocleW ot gnidoC sajniN
'''

######################################
# Reverse Each Word Of String Module #
######################################


def reverse_each_word_of_string(str):
	new_str = ""
	for sub_str in str.split():
	# DO
		new_str = new_str + sub_str[::-1] + " "
	# ENDFOR;
	new_str = new_str[:-1]
	return new_str
# END reverse_each_word_of_string.


################
# Main Program #
################

str = input("Input the string to reverse each word of the entered string: \n")
print(reverse_each_word_of_string(str))
# END.
