import sys
import re
import math

def largestPowOftwo(dec, power):
	if dec - 2**power > 0:
		return largestPowOftwo(dec, power + 1)
	elif dec - 2**power == 0:
		return power
	else:
		return power - 1

def decToBinary(dec):
	print( "decimal: ", dec)
	largestPower = largestPowOftwo(dec, 0)
	output = ""
	for power in range(largestPower, -1, -1):
		if dec - 2**power >= 0:
			output += "1"
			dec -= 2**power
		elif dec - 2**power < 0:
			output += "0"

	return output


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

print("Binary: ", decToBinary(output))
	