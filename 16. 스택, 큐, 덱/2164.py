from collections import deque

N = int(input())
main_arr = deque(range(1, N+1)) 

while len(main_arr) != 1:
    main_arr.popleft()
    main_arr.append(main_arr.popleft())

print(main_arr.pop())
