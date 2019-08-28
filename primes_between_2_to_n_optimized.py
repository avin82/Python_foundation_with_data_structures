# PROGRAM primes_between_2_to_n_optimized:

#########################
# Prime Checking Module #
#########################


def print_primes_between_2_to_n_inclusive():
	n = int(input("Input the number to print primes between 2 and the entered number: \n"))
	k = 2
	while k <= n:
	# DO
		d = 2
		is_prime = True
		while d < k:
		# DO
			if k % d == 0:
			# THEN
				is_prime = False
				break
			# ENDIF;
			d = d + 1
		# ENDWHILE;
		if is_prime:
		# THEN
			print(k)
		# ENDIF;
		k = k + 1
	# ENDWHILE;
# END print_primes_between_2_to_n_inclusive.


################
# Main Program #
################

print_primes_between_2_to_n_inclusive()
# END.
