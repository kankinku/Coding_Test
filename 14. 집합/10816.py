N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))
dic = {arr2[i]:0 for i in range(len(arr2))}

for i in arr1:
    if i in dic:
        dic[i] += 1

for i in arr2: # dic은 순서가 유지되지 않을 가능성이 있다.
    print(dic[i],end=" ")