def won_the_game(arr):
	counter, idx = [0] * (len(arr) + 1), [0] * (len(arr) + 1)
	for i in range(len(arr)):
		counter[arr[i]] += 1
		idx[arr[i]] = i + 1

	res = -1
	for i in range(len(arr) + 1):
		if counter[i] == 1:
			res = idx[i]
			break
	return res

def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		arr = list(map(int, input().split(' ')))
		res = won_the_game(arr)
		print(res)

if __name__ == '__main__':
	main()