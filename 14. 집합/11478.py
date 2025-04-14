import sys
def input_s():
    return sys.stdin.readline().strip()

fuck = input_s()
total=set()
for i in range(len(fuck)):
    for j in range(i,len(fuck)):
        total.add(fuck[i:j+1])

print(len(total))