X, Y = map(int,input().split())
A= []
B= []

for x in range(X):
   A.append(list(map(int,input().split())))

for x in range(X):
   B.append(list(map(int,input().split())))

result = []

for x in range(X):
  xline = []
  for y in range(Y):
    line = []
    line = A[x][y] + B[x][y]
    xline.append(line)
  result.append(xline)

for x in range(X):
    print(" ".join(map(str, result[x])))