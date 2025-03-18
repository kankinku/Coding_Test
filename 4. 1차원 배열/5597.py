a = []
for i in range(1,31):
  a.append(i)

for _ in range(28):
  x = int(input())
  a.remove(x)

for y in a:
  print(y)