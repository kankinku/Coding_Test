int_N, int_M = map(int,input().split())
list_card = list(map(int,input().split()))
gap = int_M

for i in range(int_N):
    for j in range(int_N):
        if list_card[i] != list_card[j]:
            for z in range(int_N):
                if list_card[i] != list_card[j] and list_card[j] != list_card[z] and list_card[i] != list_card[z]:
                    if gap > (int_M - (list_card[i] + list_card[j] + list_card[z])) and int_M - (list_card[i] + list_card[j] + list_card[z]) >= 0:
                       gap = (int_M - (list_card[i] + list_card[j] + list_card[z]))

print(int_M - gap)