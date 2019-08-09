def partition(array, low, high):
    pivot = low
    for i in range(low+1, high+1):
        if array[i] <= array[low]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[low] = array[low], array[pivot]
    return pivot

def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    
    def _quick_sort(array, low, high):
        if low >= high:
            return
        pivot = partition(array, low, high)
        _quick_sort(array, low, pivot-1)
        _quick_sort(array, pivot+1, high)

    return _quicksort(array, low, high)

if __name__ == '__main__':
	array = [54, 34, 476, 87, 23, 1, 23, 57, 978, 5, 68, 45, 876, 9, 34]
	print(quick_sort(array))
