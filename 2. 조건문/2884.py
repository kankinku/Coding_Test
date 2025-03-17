A,B = input().split()
C = int(input())

A = int(A)
B = int(B)

t = A + C // 60
m = B + C % 60

if m >= 60:
  m = m - 60
  t = t +1
if t >= 24:
  t = t - 24

print(t,m)