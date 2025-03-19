time = [3,3,3, 4,4,4, 5,5,5, 6,6,6, 7,7,7, 8,8,8,8, 9,9,9, 10,10,10,10]
A = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
S = input()
sum = 0
for i in S:
  sum += time[A.index(i)]

print(sum)