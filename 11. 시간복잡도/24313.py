A,B = map(int,input().split())
c = int(input())
n = int(input())

# B가 음수로 나올경우도 생각해야함
if (A*n + B) <= c*n and A <= c:
    print(1)
else:
    print(0)