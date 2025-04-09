import sys

count = [0]*10001
N = int(input())

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    count[num] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)
