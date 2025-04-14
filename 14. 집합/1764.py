N,M = map(int,input().split())
arr1 = []
arr2 = []
result = []
for _ in range(N):
    arr1.append(input())
for _ in range(M):
    arr2.append(input())
dic = {arr2[i] : arr2[i] for i in range(len(arr2))}

for i in arr1:
    if i in dic:
        result.append(dic[i])

print(len(result))
result=sorted(result)
print(" ".join(map(str,result)))
