def merge(left, right):
    result = []
    global inv
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
            inv += len(left)
    while len(left) > 0:
        result.append(left.pop(0))
    while len(right) > 0:
        result.append(right.pop(0))
    return result

def merge_sort(l):
    if len(l) == 1:
        return l
    left = l[:len(l)//2]
    right = l[len(l)//2:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

with open('rosalind_inv.txt') as f:
    n = int(f.readline())
    A = list(map(int, f.readline().split()))
    inv = 0
    merge_sort(A)
    print(inv)
