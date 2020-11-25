
def remove_duplicates(arr):
	res = [arr[0]]
	for i in range(1, len(arr)):
		if arr[i] != res[-1]:
			res.append(arr[i])
	return res

def n_operations(arr):
	cleaned = remove_duplicates(arr)

	counter = [1] * (len(cleaned) + 1)
	for i in range(len(cleaned)):
		counter[cleaned[i]] += 1
	counter[cleaned[0]] -= 1
	counter[cleaned[-1]] -= 1

	res = float('inf')
	for i in range(len(cleaned)):
		res = min(res, counter[cleaned[i]])
	return res

def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		arr = list(map(int, input().split(' ')))
		res = n_operations(arr)
		print(res)
	
if __name__ == '__main__':
	main()