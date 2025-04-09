target = int(input())
count = 0

for x in range(target):
    tmp = []
    A = list(map(int,str(x)))
    for i in A:
        tmp.append(i)
    tmp.append(int("".join(map(str,tmp))))
    if target == sum(tmp):
        count += 1
        print(tmp[-1])
        break
if count == 0 :
    print(0)