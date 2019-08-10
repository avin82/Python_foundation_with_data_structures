# PROGRAM all_primes_between_2_to_n:

#########################
# Prime Checking Module #
#########################


def print_primes_between_2_to_n_inclusive():
	num = int(input("Input the number to print primes between 2 and the entered number: \n"))
	for n in range(2, num + 1):
	# DO
		is_prime = True
		divisor = n - 1
		while divisor != 1:
		# DO
			if n % divisor == 0:
			# THEN
				is_prime = False
			# ENDIF;
			divisor = divisor - 1
		# ENDWHILE;
		if is_prime:
		# THEN
			print(n)
		# ENDIF;
	# ENDFOR;
# END print_primes_between_2_to_n_inclusive.


################
# Main Program #
################

print_primes_between_2_to_n_inclusive()
# END.
