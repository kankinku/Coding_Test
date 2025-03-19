S = input()

word_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in word_list:
  S = S.replace(i, "*")

print(len(S))