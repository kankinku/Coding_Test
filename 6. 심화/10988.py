S = input()

for i in range(len(S)):
  if(S[i] == S[len(S)-i-1]):
    result = 1
  else:
    result = 0
    break

print(result)
