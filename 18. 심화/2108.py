import statistics
import sys

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))
    
print(round(sum(arr)/len(arr)))
arr.sort()
print(arr[int(len(arr)//2)])
modes = statistics.multimode(arr)
if len(modes) == 1:
    print(modes[0])
else:
    modes.sort()
    print(modes[1])

print(arr[-1]-arr[0])
    