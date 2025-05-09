from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = deque(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

Q = deque()
for i in range(N):
    if A[i] == 0:
        Q.append(B.popleft())
    else:
        B.popleft()

result = []
for num in C:
    Q.appendleft(num)
    result.append(str(Q.pop()))

print(" ".join(result))


