from collections import deque

N = int(input())
arr = list(map(int, input().split()))
result = []
ball = deque((i+1, arr[i]) for i in range(N))

while ball:
    num = ball.popleft()
    result.append(str(num[0]))
    target = num[1]
    if not ball:
        break
    ball.rotate( -(target - 1) if target > 0 else -target)

print(" ".join(result))