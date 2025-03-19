A,B = input().split()
A = list(A)
B = list(B)
mid = len(A)//2

for i in range(mid):
  A[i], A[len(A)-i-1] = A[len(A)-i-1], A[i]
  B[i], B[len(A)-i-1] = B[len(A)-i-1], B[i]
  A = "".join(A)
  B = "".join(B)

print(max(int(A),int(B)))