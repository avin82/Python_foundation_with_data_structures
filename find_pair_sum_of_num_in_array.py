# PROGRAM find_pair_sum_of_num_in_array:

'''
Given a random integer array A and a number x. Find and print the pair of elements in the array which sum to x.

Array A can contain duplicate elements.

While printing a pair, print the smaller element first.

That is, if a valid pair is (6, 5) print "5 6". There is no constraint that out of 5 pairs which have to be printed in 1st line. You can print pairs in any order, just be careful about the order of elements in a pair.

Input format:
Line 1 : Integer N (Array size)
Line 2 : Array elements (separated by space)
Line 3 : Integer x

Output format:
Line 1 : Pair 1 elements (separated by space)
Line 2 : Pair 2 elements (separated by space)
Line 3 : and so on

Constraints:
1 <= N <= 1000
1 <= x <= 100

Sample Input:
9
1 3 6 2 5 4 3 2 4
7

Sample Output:
1 6
3 4
3 4
2 5
2 5
3 4
3 4
'''

########################################
# Find Pair Sum Of Num In Array Module #
########################################


def find_pair_sum_of_num_in_array(li, num):
	i = 0
	while i < len(li):
	# DO
		j = i + 1
		while j < len(li):
		# DO
			if li[i] + li[j] == num:
			# THEN
				if li[i] < li[j]:
				# THEN
					print(li[i], li[j])
				else:
					print(li[j], li[i])
				# ENDIF;
			# ENDIF;
			j = j + 1
		# ENDWHILE;
		i = i + 1
	# ENDWHILE;
# END find_pair_sum_of_num_in_array.


################
# Main Program #
################

n = int(input("Input the size of the array (or list): \n"))
li = [int(x) for x in input("Input the elements of the array (or list, separated by space): \n").split()]
num = int(input("Input the sum value to find the corresponding pair sum in the given array (or list): \n"))
find_pair_sum_of_num_in_array(li, num)
# END.
