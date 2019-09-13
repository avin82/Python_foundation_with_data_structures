# PROGRAM check_permutation:

'''
Given two strings, check if they are permutations of each other. Return true or false.

Permutation means - length of both the strings should be same and should contain same set of characters. Order of characters doesn't matter.

Note : Input strings contain only lowercase english alphabets.

Input format:
Line 1 : String 1
Line 2 : String 2

Sample Input 1:
abcde
baedc

Sample Output 1:
true

Sample Input 2:
abc
cbd

Sample Output 2:
false
'''

############################
# Check Permutation Module #
############################


def check_permutation(str1, str2):
	if len(str1) == len(str2):
	# THEN
		comparator_str = str2
		for char in str1:
		# DO
			if char not in comparator_str:
			# THEN
				return False
			else:
				index_of_char_found = comparator_str.find(char)
				comparator_str = comparator_str[:index_of_char_found] + comparator_str[index_of_char_found + 1:]
			# ENDIF;
		# ENDFOR;
		return True
	else:
		return False
	# ENDIF;
# END check_permutation.


################
# Main Program #
################

str1 = input("Input the first string: \n")
str2 = input("Input the second string: \n")
if check_permutation(str1, str2):
# THEN
	print("true")
else:
	print("false")
# ENDIF;
# END.
