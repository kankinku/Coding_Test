N, M = map(int, input().split())
arr = []
test = []

for _ in range(N):
    arr.append(input())


dic = {arr[i]: i + 1 for i in range(N)}  

for _ in range(M):
    test.append(input())

for i in test:
    if i.isdigit():  
        print(arr[int(i) - 1])  
    else:
        print(dic[i])
