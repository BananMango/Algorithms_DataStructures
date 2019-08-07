def partition(array, low, high):
	i = low - 1
	pivot = array[high]

	for j in range(low, high):
		if array[j] <= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]
		array[i + 1], array[high] = array[high], array[i + 1]
	return (i + 1)

def quick_sort(array, low = 0, high = None):
	if high is None:
		high = len(array) - 1
	if low < high:
		part = partition(array, low, high)

		quick_sort(array, low, part-1)
		quick_sort(array, part+1, high)
	return array

if __name__ == '__main__':
	array = [54, 34, 476, 87, 23, 1, 23, 57, 978, 5, 68, 45, 876, 9, 34]
	print(quick_sort(array))