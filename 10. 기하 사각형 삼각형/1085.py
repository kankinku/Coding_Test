x,y,w,h = map(int,input().split())

result = []

result.append(w-x)
result.append(x)
result.append(h-y)
result.append(y)

print(min(result))