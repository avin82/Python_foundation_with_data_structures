# PROGRAM simple_calculator:

'''
Write a program that works as a simple calculator. It reads an integer for choice.

1. If the choice is 1, 2 integers are taken for input and their sum is printed.
2. If the choice is 2, 2 integers are taken for input and their difference is printed.
3. If  the choice is 3, 2 integers are taken for input and their product is printed.
4. If  the choice is 4, 2 integers are taken for input and their quotient is printed.
5. If  the choice is 5, 2 integers are taken for input and their remainder is printed.
6. If the choice is 6, the program exits,
For any other choice, print "Invalid Operation" and ask for choice again.

Note: Each answer in next line.

Input format:
Take integers as input, in accordance to the description of the question.

Output format:
The output lines must be as prescribed in the description of the question.

Sample Input:
3
1
2
4
4
2
1
3
2
7
6

Sample Output:
2
2
5
Invalid Operation
'''

###############################################
# Perform Simple Calculator Operations Module #
###############################################


def perform_simple_calc_operations():
	choice = int(input("Input the choice of operation where 1 is add, 2 is subtract, 3 is multiply, 4 is divide, 5 is modular division, 6 is exit the program: \n"))
	count = 0
	while choice != 6:
	# DO
		count = count + 1
		if count != 1 and choice != 6:
		#THEN
			choice = int(input("Input the choice of operation where 1 is add, 2 is subtract, 3 is multiply, 4 is divide, 5 is modular division, 6 is exit the program: \n"))
		# ENDIF;
		if choice < 1 or choice > 6:
		#THEN
			print("Invalid Operation")
		elif choice >= 1 and choice <= 5:
			num1 = int(input("Input the first number for the chosen operation: \n"))
			num2 = int(input("Input the second number for the chosen operation: \n"))
			if choice == 1:
			# THEN
				print(num1 + num2)
			elif choice == 2:
				print(num1 - num2)
			elif choice == 3:
				print(num1 * num2)
			elif choice == 4:
				print(num1 // num2)
			elif choice == 5:
				print(num1 % num2)
			# ENDIF;
		# ENDIF;
	# ENDWHILE;
# END perform_simple_calc_operations.


################
# Main Program #
################

perform_simple_calc_operations()
# END.
