# PROGRAM check_prime_optimized:

########################
# Prime Checker Module #
########################


def check_prime():
	n = int(input("Input the number to check for prime: \n"))
	for d in range(2, n, 1):
	# DO
		if n % d == 0:
		# THEN
			break
		# ENDIF;
	# ENDFOR;
	else:
		print("The entered number is prime.")
# END check_prime.


################
# Main Program #
################

check_prime()
# END.
