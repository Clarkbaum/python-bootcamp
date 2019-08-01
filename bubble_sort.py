def bubble_sort(arr):
	while not is_sorted(arr):

		for index in range(1, len(arr)):
			if arr[index - 1] > arr[index]:
				temp = arr[index -1]
				arr[index - 1] = arr[index]
				arr[index] = temp

	return arr



def is_sorted(arr):
	output = True
	for index in range(1, len(arr)):
		if arr[index - 1] > arr[index]:
			output = False
	
	return output

print(bubble_sort([1,5,3,8,4,7,2,5]))
