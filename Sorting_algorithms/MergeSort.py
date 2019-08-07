def merge_sort(array):
	n = len(array)
	if n > 1:
		mid = len(array)//2
		L = array[:mid]
		R = array[mid:]
		merge_sort(L)
		merge_sort(R)

		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				array[k] = L[i]
				i += 1
			else:
				array[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			array[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			array[k] = R[j]
			j += 1
			k += 1
	return array

if __name__ == '__main__':
	array = [54, 34, 476, 87, 23, 1, 23, 57, 978, 5, 68, 45, 876, 9, 34]
	print(merge_sort(array))