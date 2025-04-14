N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dic_B = {B[i]:1 for i in range(len(B))}
count = 0

for i in A:
    if i in dic_B:
        del dic_B[i]
    else:
        count +=1

print(len(dic_B)+count)