# PROGRAM perform_string_compression:

'''
Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.

For e.g. if a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".

Note : Consecutive count of every character in input string is less than equal to 9.

Input Format:
Input string S

Output Format:
Compressed string

Sample Input:
aaabbccdsa

Sample Output:
a3b2c2dsa
'''

#####################################
# Perform String Compression Module #
#####################################


def perform_string_compression(input_str):
	compressed_str = ""
	i = 0
	while i < len(input_str):
	# DO
		j = i + 1
		if j < len(input_str) and input_str[j] != input_str[i]:
		# THEN
			compressed_str = compressed_str + input_str[i]
		else:
			char_count = 1
			while j < len(input_str) and input_str[j] == input_str[i]:
			# DO
				char_count = char_count + 1
				j = j + 1
			# ENDWHILE;
			if char_count > 1:
			# THEN
				compressed_str = compressed_str + input_str[i] + str(char_count)
			else:
				compressed_str = compressed_str + input_str[i]
			# ENDIF;
		# ENDIF;
		i = j
	# ENDWHILE;
	return compressed_str
# END perform_string_compression.


################
# Main Program #
################

input_str = input("Input the string to perform string compression on it: \n")
print(perform_string_compression(input_str))
# END.
