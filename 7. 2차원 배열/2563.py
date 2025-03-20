T = int(input())
Area = [[0 for _ in range(100)] for _ in range(100)]
count = 0

for _ in range(T):
  x,y = map(int,input().split())
  for i in range(x,x+10):
    for j in range(y,y+10):
      if Area[i][j] == 0:
        Area[i][j] = 1
        count += 1

print(count)