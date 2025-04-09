N=int(input())
arr=[]
for i in range(N):
    age,name = map(str,input().split())
    arr.append((int(age),i,name))
arr.sort()
for i in range(len(arr)):
    print(arr[i][0],arr[i][2])