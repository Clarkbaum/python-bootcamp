# Median of two sorted arrays of same size
# There are 2 sorted arrays A and B of size n each. Write an algorithm to find the median of the array 
# obtained after merging the above 2 arrays(i.e. array of length 2n). The complexity should be O(log(n)).

# median-of-two-arrays

input1 = [1, 12, 15, 26]
input2 = [2, 13, 17, 30, 77]
# output = 16
import math
junk = []

def median_of_arr(arr1, arr2):

	arr1.extend(arr2)
	arr1.sort()
	if len(arr1) % 2 == 1:
		return arr1[math.floor(len(arr1) / 2)]
	else:
		median = (arr1[int(len(arr1) / 2) - 1] + arr1[int(len(arr1) / 2)]) / 2
		return median


print(median_of_arr(input1, input2))
