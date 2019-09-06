# PROGRAM find_triplet_sum_of_num_in_array:

'''
Given a random integer array and a number x. Find and print the triplets of elements in the array which sum to x.

While printing a triplet, print the smallest element first.

That is, if a valid triplet is (6, 5, 10) print "5 6 10". There is no constraint that out of 5 triplets which have to be printed on 1st line. You can print triplets in any order, just be careful about the order of elements in a triplet.

Input format:
Line 1 : Integer N (Array Size)
Line 2 : Array elements (separated by space)
Line 3 : Integer x

Output format:
Line 1 : Triplet 1 elements (separated by space)
Line 2 : Triplet 3 elements (separated by space)
Line 3 : and so on

Constraints:
1 <= N <= 1000
1 <= x <= 100

Sample Input:
7
1 2 3 4 5 6 7 
12

Sample Output:
1 4 7
1 5 6
2 3 7
2 4 6
3 4 5
'''

###########################################
# Find Triplet Sum Of Num In Array Module #
###########################################


def find_triplet_sum_of_num_in_array(li, sum):
	i = 0
	while i < len(li):
	# DO
		j = i + 1
		while j < len(li):
		# DO
			k = j + 1
			while k < len(li):
			# DO
				if li[i] + li[j] + li[k] == sum:
				# THEN
					if li[i] <= li[j] and li[i] <= li[k]:
					# THEN
						if li[j] <= li[k]:
						# THEN
							print(li[i], li[j], li[k])
						else:
							print(li[i], li[k], li[j])
						# ENDIF;
					elif li[j] <= li[k] and li[j] <= li[i]:
					# THEN
						if li[k] <= li[i]:
						# THEN
							print(li[j], li[k], li[i])
						else:
							print(li[j], li[i], li[k])
						# ENDIF;
					else:
						if li[i] <= li[j]:
						# THEN
							print(li[k], li[i], li[j])
						else:
							print(li[k], li[j], li[i])
						# ENDIF;
					# ENDIF;
				# ENDIF;
				k = k + 1
			# ENDWHILE;
			j = j + 1
		# ENDWHILE;
		i = i + 1
	# ENDWHILE;
# END find_triplet_sum_of_num_in_array.


################
# Main Program #
################

n = int(input("Input the size of the array (or list): \n"))
li = [int(x) for x in input("Input the elements of the array (or list, separated by space): \n").split()]
sum = int(input("Input the sum value to find the corresponding triplet sum in the given array (or list): \n"))
find_triplet_sum_of_num_in_array(li, sum)
# END.
