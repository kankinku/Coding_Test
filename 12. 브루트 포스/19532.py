a,b,c,d,e,f = map(int,input().split())
first = [a,b,c]
second = [d,e,f]
result =[]

# 서로를 식에 곱하는 과정
for i in range(3):
    second[i] *= a
    first[i] *= d

# x를 제거하는 소거법 사용
for j in range(3):
    if second[j] > 0 and first[j] > 0:
        result.append(first[j] - second[j])
    else:
        result.append(first[j] + second[j])

print(result)

# x를 대입법으로 해결하는 과정
result_y =result[2] / result[1]
result_x = c - b*result_y

print(result_x, result_y)