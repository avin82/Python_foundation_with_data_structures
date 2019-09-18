# PROGRAM word_frequency:

'''
Given a string, print all the words which have frequency k, where k is provided by the user.

Print every word in a new line.

Input Format:
Line 1: String
Line 2: k, frequency number to match

Output Format:
Words matching the frequency with one word per line
'''

##############################
# Find Word Frequency Module #
##############################


def word_frequency(str, k):
	words_list = str.split()
	frequency_dict = {}
	for word in words_list:
	# DO
		if word in frequency_dict:
		# THEN
			frequency_dict[word] = frequency_dict[word] + 1
		else:
			frequency_dict[word] = 1
		# ENDIF;
	# ENDFOR;
	for word in frequency_dict:
	# DO
		if frequency_dict[word] == k:
		# THEN
			print(word)
		# ENDIF;
	# ENDFOR;
# END word_frequency.


################
# Main Program #
################

str = input("Input the string to find the word frequency: \n")
frequency_num = int(input("Input the frequency (in number) to find the words in the entered string which match the frequency: \n"))
word_frequency(str, frequency_num)
# END.
