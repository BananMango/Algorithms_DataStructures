def selection_sort(array):
	n = len(array)
	for i in range(n):
		min_index = i
		for j in range(i+1, n):
			if array[min_index] > array[j]:
				min_index = j
		array[i], array[min_index] = array[min_index], array[i]
	return array

if __name__ == '__main__':
	array = [54, 34, 476, 87, 23, 1, 23, 57, 978, 5, 68, 45, 876, 9, 34]
	print(selection_sort(array))