# PROGRAM power_of_num:

'''
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.

Input format:
Two integers x and n (separated by space)

Output Format:
x^n (i.e. x raise to the power n)

Sample Input 1:
3 4

Sample Output 1:
81

Sample Input 2:
2 5

Sample Output 2:
32
'''

##########################
# Power Of Number Module #
##########################


def power_of_num(num, pow):
    if pow == 0:
	# THEN
        return 1
	# ENDIF;
    return num * power_of_num(num, pow - 1)
# END power_of_num.


################
# Main Program #
################

str_input = input("Input a number x and a power value n (separated by space) to find x to the power n: \n")
x, n = int(str_input.split()[0]), int(str_input.split()[1])
print(power_of_num(x, n))
# END.
