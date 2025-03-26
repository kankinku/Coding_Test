A = []
for _ in range(3):
    A.append(int(input()))

if sum(A) != 180:
    print("Error")
elif A.count(60) == 3:
    print("Equilateral")
elif A[0] == A[1] or A[1] == A[2] or A[2] == A[0]:
    print("Isosceles")
else:
    print("Scalene")

