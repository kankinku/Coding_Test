while True:
    A = sorted(map(int,input().split()))

    if A.count(0) == 3:
        break

    if A[2] < A[1] + A[0]:
        if A[0] == A[1] and A[1] == A[2]:
            print("Equilateral")
        elif A[0] == A[1] or A[1] == A[2] or A[2] == A[0]:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")