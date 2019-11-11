def binarySearch(k, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        item = arr[mid]
        if item == k:
            return mid + 1
        elif item > k:
            high = mid - 1
        else:
            low = mid + 1
    return -1

with open('rosalind_bins.txt') as f:
    n = int(f.readline())
    m = int(f.readline())
    A = list(map(int, f.readline().split()))
    K = list(map(int, f.readline().split()))

    
with open('rosalind_bins_out.txt', 'w') as f:
        f.write(' '.join(map(str, [binarySearch(k, A) for k in K])))
    
