X = []
Y = []

for _ in range(3):
    x,y = list(map(int,input().split()))
    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) != 2: x = X[i]
    if Y.count(Y[i]) != 2: y = Y[i]
print(x,y)