S = input().upper()
maxNum = 0

for i in range(len(S)):
  if maxNum < S.count(S[i]):
    maxNum = S.count(S[i])

if S.count(S[i]) > 2:
  print("?")
else:
  print(maxNum)
  