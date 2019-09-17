# PROGRAM row_wise_sum_2d_array:

'''
Given a 2D integer array of size M*N, find and print the sum of ith row elements separated by space.

Input Format:
Line 1 : Two integers M and N (separated by space)
Line 2 : Matrix elements of each row (separated by space)

Output Format:
Sum of every ith row elements (separated by space)

Constraints:
1 <= M, N <= 10^3

Sample Input:
4 2
1 2 3 4 5 6 7 8

Sample Output:
3 7 11 15
'''

########################################
# Find Row Wise Sum Of 2d Array Module #
########################################


def rowWiseSum(arr):
	res = []
	for row in arr:
	# DO
		sum = 0
		for element in row:
		# DO
			sum = sum + element
		# ENDFOR;
		res.append(sum)
	# ENDFOR;
	return res


################
# Main Program #
################

m, n = (int(i) for i in input().strip().split(' '))
l = [int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
l = rowWiseSum(arr)
print(*l)
# END.
