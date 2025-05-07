n = int(input())
arr = []
total = 0

for i in range(n):
    num = int(input())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)

if len(arr) == 0:
    print(0)
else:
    for i in range(len(arr)):
        total += arr[i]
    print(total)