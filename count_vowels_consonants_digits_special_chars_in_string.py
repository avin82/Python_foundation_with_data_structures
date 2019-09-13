# PROGRAM count_vowels_consonants_digits_special_chars_in_string:

'''
Find and return the number of vowels, consonants, digits and special characters in a given string.

Input Format:
String

Output Format:
Number of vowels, consonants, digits and special characters separated by space

Sample Input:
zabcdaimleu#$23 82!

Sample Output:
5 6 4 4
'''

#################################################################
# Count Vowels Consonants Digits Special Chars In String Module #
#################################################################


def count_vowels_consonants_digits_special_chars_in_string(str):
	v, c, d, s = 0, 0, 0, 0
	for char in str:
	# DO
		if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
		# THEN
			if char.lower() in ['a', 'e', 'i', 'o', 'u']:
			# THEN
				v = v + 1
			else:
				c = c + 1
			# ENDIF;
		elif (char >= '0' and char <= '9'):
		# THEN
			d = d + 1
		else:
			s = s + 1
		# ENDIF;
	# ENDFOR;
	return v, c, d, s
# END count_vowels_consonants_digits_special_chars_in_string.


################
# Main Program #
################

str = input("Input the string: \n")
v, c, d, s = count_vowels_consonants_digits_special_chars_in_string(str)
print(v, c, d, s)
# END.
