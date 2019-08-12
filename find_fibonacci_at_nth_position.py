# PROGRAM find_fibonacci_at_nth_position:

'''
Nth term of fibonacci series F(n) is calculated using following formula -

 F(n) = F(n-1) + F(n-2)

 Provided N you have to find out the Nth Fibonacci Number. Also F(1) = F(2) = 1.

 Input Format:
 Integer n

 Constraints:
 Time Limit: 1 second

 Output Format:
 Nth Fibonacci term i.e. F(n)

 Sample Input:
 4

 Sample Output:
 3
'''

#########################################
# Find Fibonacci At nth Position Module #
#########################################


def find_fibonacci_at_nth_position():
	position = int(input("Please input the position (i.e. positive integer value) for which you want to find the Fibonacci number in the Fibonacci series: \n"))
	temp_pos = position
	first_num = 1
	second_num = 1
	if (position == 1) or (position == 2):
	# THEN
		return first_num
	else:
		while position != 2:
		# DO
			fib = first_num + second_num
			first_num = second_num
			second_num = fib
			position = position - 1
		# ENDWHILE;
		return fib
	# ENDIF;
# END find_fibonacci_at_nth_position.


################
# Main Program #
################

print(find_fibonacci_at_nth_position())
# END.
