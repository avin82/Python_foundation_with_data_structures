# PROGRAM avg_three_numbers:

'''
Find average marks

Write a program to input marks of three tests of a student (all integers). Then calculate and print the average of all test marks.

Input format:
3 Test marks (in different lines)

Output format:
Average

Sample Input 1:
3
4
6

Sample Output 1:
4.333333333333333

Sample Input 2:
5
10
5

Sample Output 2:
6.666666666666667
'''

##########################
# Finding Average Module #
##########################


def find_avg():
	num1 = int(input("Input first number: \n"))
	num2 = int(input("Input second number: \n"))
	num3 = int(input("Input third  number: \n"))
	return (num1 + num2 + num3) / 3


################
# Main Program #
################

avg = find_avg()
print("Average of user inputted numbers is {}".format(avg))
# END.
