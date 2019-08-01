# Input: arr[] = {1, 2, 4,, 6, 3, 7, 8}
# Output: 5

# Input: arr[] = {1, 2, 3, 5}
# Output: 4

def missing_num(arr):
	for index in range(1, len(arr)):
		if arr[index - 1] + 1 != arr[index]:
			return arr[index - 1] + 1


print(missing_num([1, 2, 3, 5]))