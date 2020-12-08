
def unique(arr):
    res = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != res[-1]:
            res.append(arr[i])
    return res


def n_operations(arr):
    cleaned = unique(arr)

    occurences = {}
    for el in cleaned:
        if el in occurences.keys():
            occurences[el] += 1
        else:
            occurences[el] = 1

    best = len(cleaned)
    for el in cleaned:
        best = min(best, occurences[el] + 1 -
                   (cleaned[0] == el) - (cleaned[-1] == el))
    return best


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split(' ')))
        res = n_operations(arr)
        print(res)


if __name__ == '__main__':
    main()
