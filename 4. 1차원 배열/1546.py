T = int(input())

score = list(map(int,input().split()))
total = 0

M = max(score)

for i in range(T):
  total += score[i]/M*100

print(total/T)