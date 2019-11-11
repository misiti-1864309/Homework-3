from random import randrange

def partition(arr):
    p = arr[randrange(len(arr))]
    left, right, equal = [], [], []
    for i in arr:
        if i < p:
            left.append(i)
        elif i > p:
            right.append(i)
        else:
            equal.append(i)
    return left, equal, right

def selection(arr, k):
    l, v, r = partition(arr)
    if k <= len(l):
        return selection(l, k)
    elif k <= len(l) + len(v):
        return v[0]
    else:
        return selection(r, k-len(l)-len(v))

with open('rosalind_med.txt') as f:
    n = int(f.readline())
    A = list(map(int, f.readline().split()))
    k = int(f.readline())
    print(selection(A, k))
