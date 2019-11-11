def partition(arr):
    p = arr[0]
    left, right, equal = [], [], []
    for i in arr:
        if i < p:
            left.append(i)
        elif i > p:
            right.append(i)
        else:
            equal.append(i)
    return left + equal + right

with open('rosalind_par3.txt') as f:
    n = int(f.readline())
    A = list(map(int, f.readline().split()))

with open('rosalind_par3_out.txt', 'w') as f:
    f.write(' '.join(map(str, partition(A))))
