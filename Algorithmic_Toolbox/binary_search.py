
def binary_search(arr, val):
    l = 0
    r = len(nums)
    while l + 1 < r:
        m = l + (r - l) // 2
        if nums[m] > target:
            r = m
        else:
            l = m
    if nums[l] == target:
        return l
    else: return -1

if __name__ == '__main__':
	array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]  
	element = 7     
	print("Searching for {} in {}".format(element, array))
	print("Index of {}: {}".format(element, binary_search(array, element)))
