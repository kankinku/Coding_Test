T = int(input())

for _ in range(T):
  R, P =input().split()
  R = int(R) 
  for i in P:
    for _ in range(R):
      print(i,end="")
  print()