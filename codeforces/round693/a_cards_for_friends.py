def check_cuts(w, h, n):
	res = 1
	while w % 2 == 0:
		res = res * 2
		w = w // 2
	while h % 2 == 0:
		res = res * 2
		h = h // 2

	if res >= n:
		return 'Yes'
	else:
		return 'No'

def main():
	n = int(input())
	for i in range(n):
		w, h, n = list(map(int, input().split(' ')))
		print(check_cuts(w, h, n))

if __name__ == '__main__':
	main()