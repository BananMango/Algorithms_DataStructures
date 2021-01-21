def play_game(arr):
	score = [None] * len(arr)
	for i in reversed(range(0, len(arr))):
		score[i] = arr[i]
		j = i + arr[i]
		if j < len(arr):
			score[i] += score[j]
	return max(score)

def main():
	n = int(input())
	for i in range(n):
		t = int(input())
		arr = list(map(int, input().split(' ')))
		print(play_game(arr))

if __name__ == '__main__':
	main()