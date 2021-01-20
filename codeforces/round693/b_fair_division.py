def check_weights(arr):
	cnt1, cnt2 = 0, 0
	for el in arr:
		if el == 1:
			cnt1 += 1
		else:
			cnt2 += 1

	if (cnt1 + cnt2 * 2) % 2 != 0:
		return 'No'
	else:
		total_sum = (cnt1 + 2 * cnt2) / 2
		if (total_sum % 2 == 0 or (total_sum % 2 == 1 and cnt1 != 0)):
			return 'Yes'
		else:
			return 'No'


	

def main():
	n = int(input())
	for i in range(n):
		arr_len = int(input())
		arr = list(map(int, input().split(' ')))
		print(check_weights(arr))

if __name__ == '__main__':
	main()