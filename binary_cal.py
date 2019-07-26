import sys
import re
import math

def decToBinary(dec, power, output):
	junk = dec - 2**power
	if dec - 2**power > 0:
		decToBinary(dec, power + 1, output)
	else:
		output += "1"
		decToBinary(dec - 2**(power - 1), 0, output)
		# return decToBinary(dec, power + 1)

print(sys.argv)
decimals = []

if len(sys.argv) != 4 :
	sys.exit("please provide two binary arguments followed by either x, /, +, or -")

for arg in range(1, len(sys.argv) - 1):
	arg = sys.argv[arg]
	matches = re.findall(r'^[0-1]+$', arg)
	if len(matches) == 0:
		sys.exit("please use binary numbers as input")

	if arg != matches[0]:
		sys.exit("please use binary numbers as input")

	decimal = 0
	power = 0
	for index in range(len(arg) -1 , -1, -1):
		
		value = arg[index]
		if value == "1" :
			decimal += 2**power

		power += 1

	decimals.append(decimal)

operator = sys.argv[3]
output = 0

if(operator == "+"):
	output = decimals[0] + decimals[1]
elif operator == "x":
	output = decimals[0] * decimals[1]
elif operator == "-":
	output = decimals[0] - decimals[1]
elif operator == "/":
	output = math.floor(decimals[0] / decimals[1])
else:
	sys.exit("operator not supported")

print(decToBinary(output, 0, ""))







	