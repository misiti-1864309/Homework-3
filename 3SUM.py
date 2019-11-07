from collections import defaultdict
def three_sum(A):
    d = defaultdict(list)
    for j in range(n):
        d[A[j]].append(j)
    for j in range(n):
        for k in range(j+1,n):
            l = -(A[j]+A[k])
            if len(d[l]) > 0:
                return j+1, k+1, d[l][0]+1
    return [-1]
                    
out = []
with open('rosalind_3sum.txt') as f:
    k, n = map(int, f.readline().split())
    for i in range(k):
        A = list(map(int, f.readline().split()))
        out.append(' '.join(map(str, three_sum(A))))
        
                    

with open('rosalind_3sum_out.txt', 'w') as f:
    f.write('\n'.join(out))