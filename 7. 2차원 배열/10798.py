line = []
result = []
count = 0

for _ in range(5):
  S = input()
  line.append(list(S))
  if count < len(list(S)):
    count = len(list(S))

for x in range(count):
  for i in range(len(line)):
    if x < len(line[i]):
      result.append(line[i][x])

print("".join(map(str,result)))