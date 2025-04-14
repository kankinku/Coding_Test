N = int(input())
have_arr = list(map(int,input().split()))
dic = {have_arr[i] : 1 for i in range(len(have_arr))}
targetNum = int(input())
input_arr = list(map(int,input().split()))

for i in input_arr:
    print(dic.get(i,0),end=" ") 