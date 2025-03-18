N,M = map(int, input().split())
basket = []
for _ in range(N):
  basket.append(0)


for _ in range(M):
  i,j,k = map(int,input().split())
  for x in range(i,j+1):
    basket[x-1] = k

print(" ".join(map(str,basket)))

