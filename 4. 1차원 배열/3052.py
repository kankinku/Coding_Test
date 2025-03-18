target = []

for _ in range(10):
  x = int(input())
  target.append(x%42)

print(len(list(set(target))))


