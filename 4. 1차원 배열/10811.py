N,M = map(int,input().split())

target = []
for i in range(1,N+1):
  target.append(i)

for j in range(M):
  x,y = map(int,input().split())
  t = (y-x+1) //2
  for k in range(t):
    target[x+k-1], target[y-k-1] = target[y-k-1], target[x+k-1]

print(" ".join(map(str,target)))