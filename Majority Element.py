out = []
with open('rosalind_maj.txt') as f:
    k, n = map(int, f.readline().split())
    for i in range(k):
        arr = list(map(int, f.readline().split()))
        app = False
        for i in set(arr):
            if arr.count(i) > n//2:
                out.append(i)
                app = True
        if app == False:
            out.append(-1)

with open('rosalind_maj_out.txt', 'w') as f:
    f.write(' '.join(map(str, out)))
        