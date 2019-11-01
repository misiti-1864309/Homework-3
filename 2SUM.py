out = []
with open('rosalind_2sum.txt') as f:
    k, n = map(int, f.readline().split())
    for i in range(k):
        A = list(map(int, f.readline().split()))
        for p in range(len(A)):
            found = False
            for q in range(p+1, len(A)):
                if A[p] == -A[q]:
                    found = True
                    break
            if found:
                break
        if found:
            out.append(str(p+1)+' '+str(q+1))
        else:
            out.append('-1')

with open('rosalind_2sum_out.txt', 'w') as f:
    f.write('\n'.join(out))
                
        