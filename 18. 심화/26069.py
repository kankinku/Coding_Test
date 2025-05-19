# N = int(input())
# dance = set(["ChongChong"])
# count = 1
# for _ in range(N):
#     A, B = input().split()
#     if A in dance and B not in dance:
#         dance.add(B)
#         count += 1
#     elif B in dance and A not in dance:
#         dance.add(A)
#         count += 1

# print(count)

N = int(input())
dance = set(["ChongChong"])
for _ in range(N):
    A, B = input().split()
    if A in dance or B in dance:
        dance.add(B)
        dance.add(A)


print(len(dance))
