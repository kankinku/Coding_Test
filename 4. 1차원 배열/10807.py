N = int(input())
V = input().split()
target = input()
count = 0

for i in range(N):
  if V[i] == target: 
    count += 1

print(count)