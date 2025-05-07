from collections import deque
import sys


input = sys.stdin.readline

Time = int(input())
deck = deque()

for _ in range(Time):
    command = list(map(int,input().split()))
    if command[0] == 1:
        deck.appendleft(command[1])
    elif command[0] == 2:
        deck.append(command[1])
    elif command[0] == 3:
        print(deck.popleft() if deck else -1)
    elif command[0] == 4:
        print(deck.pop() if deck else -1)
    elif command[0] == 5:
        print(len(deck))
    elif command[0] == 6:
        print(0 if deck else 1)
    elif command[0] == 7:
        if deck:
            n = deck.popleft()
            deck.appendleft(n)
            print(n)
        else:
            print(-1)
    elif command[0] == 8:
        if deck:
            n = deck.pop()
            deck.append(n)
            print(n)
        else:
            print(-1)