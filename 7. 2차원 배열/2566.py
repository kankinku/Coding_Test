I = []
for _ in range(9):
  I.append(list(map(int,input().split())))


# Max = []
# Maxindex = []
# for x in range(9):
#   Max.append(max(I[x]))
#   Maxindex.append(I[x].index(max(I[x])))
# print(max(Max))
# print(Max.index(max(Max))+1, Maxindex[Max.index(max(Max))]+1 )

max_Num = -1
row, col = 0, 0

for i in range(9):
  for j in range(9):
    if I[i][j] > max_Num:
      max_Num = I[i][j]
      row, col = i+1 , j+1

print(max_Num)
print(row, col)