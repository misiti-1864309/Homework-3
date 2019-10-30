def InsertionSort(A, n):
    swaps = 0
    for i in range(1,n):
        k = i
        while k > 0 and A[k] < A[k-1]:
            A[k-1], A[k] = A[k], A[k-1]
            k -= 1
            swaps += 1
    return swaps
