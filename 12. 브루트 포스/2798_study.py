import itertools

# pool = ['a','b','c']
# print(list(map(''.join, itertools.permutations(pool,2))))
# print(list(map(''.join, itertools.permutations(pool))))


N,M = map(int,input().split())
card = list(map(int,input().split()))
top_score = 0

for i in itertools.combinations(card,3):
    temp_card = sum(i)
    if top_score < temp_card <= M:
        top_score = temp_card

print(top_score)

