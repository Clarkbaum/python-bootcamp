# Search an element in a sorted and rotated array
# An element in a sorted array can be found in O(log n) time via binary search. 
# But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. 
# So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array 
# in O(log n) time.

# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
#          key = 3
# Output : Found at index 8

# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
#          key = 30
# Output : Not found

# Input : arr[] = {30, 40, 50, 10, 20}
#         key = 10   
# Output : Found at index 3

import math

output = ''
def search_arr(origArr, target):
	
	rotate_point = -1
	
	for index in range(1, len(origArr)):
		if origArr[index -1] > origArr[index]:
			rotate_point = index
	
	# left_arr = arr[0:rotate_point]
	# right_arr = arr[rotate_point:]
	# junk = []

	

	def search(arr, target, middle):
		global output
		print("arr", arr)
		left_arr = arr[0:middle]
		right_arr = arr[middle:]
		# middle = arr[math.floor(len(arr) / 2)]
		print("middle", middle)
		print("left_arr", left_arr)
		print("right_arr", right_arr)
		if len(arr) == 0:
			print("arr is zero returning")
			return
		elif len(arr) == 1 and arr[0] != target:
			print("not last val returning")
			return
		elif arr[middle] == target:
			output = f'Found at Index {middle}'
			return
		else:
			search(left_arr, target, math.floor(len(left_arr) / 2))
			search(right_arr, target, math.floor(len(right_arr) / 2))

		if output == '':
			output = "Not Found"
		
		return output


	return search(origArr, target, rotate_point)



print(search_arr([5, 6, 7, 8, 9, 10, 1, 2, 3], 3))
