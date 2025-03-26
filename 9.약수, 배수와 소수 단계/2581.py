M = int(input())
N = int(input())

result = []

for i in range(M,N+1):
    if i > 1:
        for j in range(2,i+1):
            if i%j == 0:
                if i == j:
                    result.append(i)
                break

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))