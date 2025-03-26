N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    if A[i] == 1:
        A[i] = "out"
    else:
        for j in range(2,A[i]):
            if A[i]%j == 0:
                A[i] = "out"
                break

print(N - A.count("out"))



### 피드백 

# N = int(input())
# data = list(map(int,input().split()))
# count = 0

# for x in data:
#     for i in range(2, x+1):
#         if x%i == 0:
#             if x == i:
#                 count += 1
#             break

# print(count)
