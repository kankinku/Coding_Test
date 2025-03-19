N = int(input())
for i in range(1,N):
  print(" "*(N-i) + "*"*(i+(i-1)))
for j in range(N,0, -1):
  print(" "*(N-j) + "*"*(2*j-1))