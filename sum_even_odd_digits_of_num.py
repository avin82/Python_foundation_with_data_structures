# PROGRAM sum_even_odd_digits_of_num:

'''
Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.

Digits means numbers not the places. That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.

Input format:
Integer N

Output format:
Sum_of_Even_Digits Sum_of_Odd_Digits
(Print first even sum and then odd sum separated by space)

Sample Input:
1234

Sample Output:
6 4
'''

####################################
# Print Sum Even Odd Digits Module #
####################################


def print_sum_even_odd_digits_of_num():
	num = int(input("Input number for which sum of its even and odd digits need to be calculated separately: \n"))
	sum_evens = 0
	sum_odds = 0
	while num != 0:
	# DO
		if (num % 10) % 2 == 0:
		# THEN
			sum_evens = sum_evens + (num % 10)
		else:
			sum_odds = sum_odds + (num % 10)
		# ENDIF;
		num = num // 10
	# ENDWHILE;
	print(sum_evens, sum_odds)
# END find_sum_even_odd_digits_of_num.


################
# Main Program #
################

print_sum_even_odd_digits_of_num()
# END.

