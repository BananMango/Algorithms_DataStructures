def insertion_sort(array):
	n = len(array)
	for i in range(1, n):
		key = array[i]
		j = i-1
		while j >= 0 and key < array[j]:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key
	return array

if __name__ == '__main__':
	array = [54, 34, 476, 87, 23, 1, 23, 57, 978, 5, 68, 45, 876, 9, 34]
	print(insertion_sort(array))