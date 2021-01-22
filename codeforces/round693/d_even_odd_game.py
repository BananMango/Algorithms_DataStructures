def play_game(arr):
	res = 0
	arr.sort(reverse=True)
	
	for i in range(len(arr)):
		if i % 2 == 0:
			if arr[i] % 2 == 0:
				res += arr[i]
		else:
			if arr[i] % 2 == 1:
				res -= arr[i]

	if res == 0:
		return 'Tie'
	elif res > 0:
		return 'Alice'
	else:
		return 'Bob'

def main():
	n = int(input())
	for i in range(n):
		t = int(input())
		arr = list(map(int, input().split(' ')))
		print(play_game(arr))

if __name__ == '__main__':
	main()