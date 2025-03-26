A = sorted(map(int,input().split()))

while True:
    if A[2] < A[1] + A[0]:
        print(sum(A))
        break
    else:
        A[2] -= 1