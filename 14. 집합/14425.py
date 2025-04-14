N = int(input())
dic = {}
for _ in range(N):
    name, state = map(str,input().split())
    if state == 'leave':
        del dic[name]
    else:
        dic[name] = state

dic = sorted(dic,reverse=True)
for i in range(len(dic)):
    print(dic[i])


