T = int(input())
x = []
y = []
for _ in range(T):
    X, Y = map(int,input().split())
    x.append(X)
    y.append(Y)

print((max(x) - min(x)) * (max(y) - min(y)))
