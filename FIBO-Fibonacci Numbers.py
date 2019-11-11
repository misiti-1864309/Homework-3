def fib(n):
    d = {0: 0, 1: 1}
    if n in d.keys():
        return d[n]
    else:
        d[n] = fib(n-1) + fib(n-2)
        return d[n]

with open('rosalind_fibo.txt') as f:
    n = int(f.readline())
print(fib(n))
