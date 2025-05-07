from collections import deque


N, K = map(int,input().split())
arr = deque(i for i in range(1,N+1))
result = []
count = 0

while arr:
    if count != K-1:
        arr.append(arr.popleft())
        count += 1
    else: 
        result.append(arr.popleft())
        count = 0

print("<"+", ".join(map(str,result))+">")