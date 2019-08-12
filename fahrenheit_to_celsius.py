# PROGRAM fahrenheit_to_celsius:

'''
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

Input Format:
3 integers - S, E and W respectively

Output Format:
Fahrenheit to Celsius conversion table. One line for every Fahrenheit and corresponding Celsius value. On Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")

Sample Input:
0
100
20

Sample Output:
0   -17
20  -6
40  4
60  15
80  26
100 37
'''

########################################
# Convert Fahrenheit To Celsius Module #
########################################


def convert_fahrenheit_to_celsius():
	start_fahrenheit = int(input("Input the start value in fahrenheit of the series which needs to be converted in celsius: \n"))
	end_fahrenheit = int(input("Input the end value in fahrenheit of the series which needs to be converted in celsius: \n"))
	step_size = int(input("Input the step size value for getting the fahrenheit values in the series which need to be converted to celsius: \n"))
	while start_fahrenheit <= end_fahrenheit:
	# DO
		print(start_fahrenheit, int((start_fahrenheit - 32) * 5 / 9), sep="\t")
		start_fahrenheit = start_fahrenheit + step_size
	# ENDWHILE;
# END.


################
# Main Program #
################

convert_fahrenheit_to_celsius()
# END.
