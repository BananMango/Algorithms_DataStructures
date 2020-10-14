
def binary_search(arr, val):
	l = 0
	r = len(arr)
	mid = 0

	while (l+1 < r):
		mid = l + (r - l) // 2
		if val > arr[mid]:
			l = mid
		else:
			r = mid
	if arr[mid] == val:
		return mid
	else:
		return -1

if __name__ == '__main__':
	array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]  
	element = 7     
	print("Searching for {} in {}".format(element, array))
	print("Index of {}: {}".format(element, binary_search(array, element)))