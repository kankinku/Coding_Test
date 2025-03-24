N = int(input())
A = list(map(int,input().split()))
print(A)
count = 0

for i in range(len(A)-1):
    for j in range(1,A[i]+1):
        if A[i-1]%j == 0 :
            if j != A or j != 1:
                count += 1
    if count != 0:
        A.remove(A[i])
        i+=1
print(len(A))
    