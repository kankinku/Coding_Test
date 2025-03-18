N,M = map(int,input().split())
A = []

for x in range(N):
  A.append(x+1)

for _ in range(M):
  i,j = map(int, input().split())
  A[i-1], A[j-1] = A[j-1], A[i-1]

print(" ".join(map(str,A)))