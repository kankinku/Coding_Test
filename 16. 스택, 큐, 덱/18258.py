import sys
from collections import deque

input = sys.stdin.readline

Time = int(input())
arr = deque()

for _ in range(Time):
    command = input().split()
    
    if command[0] == "push":
        arr.append(command[1])
    elif command[0] == "pop":
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(arr))
    elif command[0] == "empty":
        print(0 if arr else 1)
    elif command[0] == "front":
        print(arr[0] if arr else -1)
    elif command[0] == "back":
        print(arr[-1] if arr else -1)
