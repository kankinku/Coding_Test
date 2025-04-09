M,N = map(int,input().split())

start_color = []
for j in range(M):
    Line = list(map(str,input()))
    start_color.append(Line[0])
    if j >= 1:
        if start_color[j-1] == start_color[j]:
            Line[0] = 1
        else:
            Line[0] = 0

    for i in range(1,N):
        if Line[i] == Line[i-1]:
            Line[i] = 1
        else:
            Line[i] = 0
    print(Line)