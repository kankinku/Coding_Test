# 1. 연속으로 나오는것은 상관없음
# 2. 연속으로 나오는것이 끝나면 그 이후로 나오면 안됨


T = int(input())
count = 0
a = 0

for _ in range(T):
  a = 0
  S = list(input())
  for i in range(len(S)-1):
    if S[i] == S[i+1]:
      S[i] = ""
    else:
      if S.count(S[i]) > 1:
        a += 1
  if a == 0:
    count += 1

print(count)

    
