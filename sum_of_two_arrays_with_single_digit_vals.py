# PROGRAM sum_of_two_arrays_with_single_digit_vals:

'''
Two random integer arrays are given A1 and A2, in which numbers from 0 to 9 are present at every index (i.e. single digit integer is present at every index of both given arrays).

You need to find sum of both the input arrays (like we add two integers) and put the result in another array i.e. output array (output arrays should also contain only single digits at every index).

The size A1 & A2 can be different.

Note : Output array size should be 1 more than the size of bigger array and place 0 at the 0th index if there is no carry. No need to print the elements of output array.

Input format:
Line 1 : Integer n1 (A1 Size)
Line 2 : A1 elements (separated by space)
Line 3 : Integer n2 (A2 Size)
Line 4 : A2 elements (separated by space)

Output Format:
Output array elements (separated by space)

Constraints :
1 <= n1, n2 <= 10^6

Sample Input 1:
3
6 2 4
3
7 5 6

Sample Output 1:
1 3 8 0 

Sample Input 2:
3
8 5 2
2
1 3

Sample Output 2:
0 8 6 5 
'''

###################################################
# Sum Of Two Arrays With Single Digit Vals Module #
###################################################


def find_sum_of_arrays_with_single_digit_vals(n1, a1, n2, a2):
	arr = [0 for x in range(max(n1, n2) + 1)]
	i, j, index_of_sum, carry = n1 -1, n2 - 1, len(arr) - 1, 0
	while i >= 0 and j >= 0:
	# DO
		sum = a1[i] + a2[j] + carry
		i, j = i - 1, j - 1
		if sum >= 10:
		# THEN
			if sum == 10:
			# THEN
				arr[index_of_sum] = 0
			else:
				arr[index_of_sum] = sum - 10
			# ENDIF;
			carry = 1
			index_of_sum = index_of_sum - 1
		else:
			arr[index_of_sum] = sum
			carry = 0
			index_of_sum = index_of_sum - 1
		# ENDIF;
	# ENDWHILE;

	if j < 0:
	# THEN
		while i >= 0:
		# DO
			if carry:
			# THEN
				arr[index_of_sum] = a1[i] + carry
				carry = 0
			else:
				arr[index_of_sum] = a1[i]
			# ENDIF;
			index_of_sum = index_of_sum - 1
			i = i - 1
		# ENDWHILE;
	elif i < 0:
	# THEN
		while j >= 0:
		# DO
			if carry:
			# THEN
				arr[index_of_sum] = a2[j] + carry
				carry = 0
			else:
				arr[index_of_sum] = a2[j]
			index_of_sum = index_of_sum - 1
			j = j - 1
			# ENDIF;
		# ENDWHILE;
	# ENDIF;
	
	if carry:
	# THEN
		arr[0] = 1
	# ENDIF;
	return arr
# END find_sum_of_arrays_with_single_digit_vals.


################
# Main Program #
################

n1 = int(input("Input the size of first array (or list): \n"))
a1 = [int(x) for x in input("Input the elements of first array (or list, separated by space): \n").split()]
n2 = int(input("Input the size of second array (or list): \n"))
a2 = [int(x) for x in input("Input the elements of second array (or list, separated by space): \n").split()]
sum_arr = find_sum_of_arrays_with_single_digit_vals(n1, a1, n2, a2)
[print(x, end=" ") for x in sum_arr]

