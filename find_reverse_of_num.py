# PROGRAM find_reverse_of_num:

'''
Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

Input format:
Integer N

Constraints:
Time Limit: 1 second

Output format:
Corresponding reverse number

Sample Input 1:
1234

Sample Output 1:
4321

Sample Input 2:
1980

Sample Output 2:
891
'''

#################################
# Find Reverse Of Number Module #
#################################


def find_reverse_of_num():
	num = int(input("Input the number to calculate its reverse: \n"))
	rev = 0
	while num != 0:
	# DO
		rev = rev * 10 + num % 10
		num = num // 10
	# ENDWHILE;
	return rev
# END find_reverse_of_num.


################
# Main Program #
################

print(find_reverse_of_num())
# END.
