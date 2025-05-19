from itertools import combinations


T = int(input())

def fac(N):
    if N == 0:
        return 1
    else:
        return N * fac(N-1)

for i in range(T):
    N,M = map(int,input().split())
    print(int(fac(M) // (fac(M-N) * fac(N))))