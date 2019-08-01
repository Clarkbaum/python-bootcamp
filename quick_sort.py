import math

# def quick_sort(arr):
# 	pivot = arr[math.floor(len(arr) / 2)]
# 	left_arr = []
# 	right_arr = []
# 	if len(arr) == 1:
# 		return arr
	
# 	for index in range(len(arr)):
# 		if arr[index] < pivot:
# 			left_arr.append(arr[index])
# 		elif arr[index] >= pivot:
# 			right_arr.append(arr[index])

# 	quick_sort(left_arr)
# 	quick_sort(right_arr)

# quick_sort([4,7,2,4,9,6,4,2,1])
# left_arr = [4,7,2,4,6,4,2,1]
# 	left_arr = [4,2,4,4,2,1,]
#	right_arr = [7,6]
# right_arr = [9]
#	left_arr = []
#	right_arr = [9]

# TODO deal with many repeats

def quick_sort(arr):
	output = []
	def search(arr):
		# print(arr)
		left_arr = []
		right_arr = []
		if len(arr) == 1:
			return arr[0]
		if len(arr) == 0:
			return
		pivot = arr[math.floor(len(arr) / 2)]
		
		# print(pivot)
		for index in range(len(arr)):
			if arr[index] < pivot:
				left_arr.append(arr[index])
			elif arr[index] > pivot:
				right_arr.append(arr[index])

		left_val = search(left_arr)
		right_val = search(right_arr)
		if(left_val != None):
			output.append(left_val)

		output.append(pivot)

		if(right_val != None):
			output.append(right_val)

	search(arr)

	return output


print(quick_sort([4,7,2,4,9,6,4,3,1]))
