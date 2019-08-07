def bubble_sort(array):
	n = len(array)
	for i in range(n):
		for j in range(0, n-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array

if __name__ == '__main__':
	array = [54, 34, 476, 87, 23, 1, 23, 57, 978, 5, 68, 45, 876, 9, 34]
	print(bubble_sort(array))