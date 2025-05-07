state = "Nice"
T = int(input())
input_arr = list(map(int, input().split()))
stack_arr = []
result = 1 # 이번에 나와야하는 숫자

for i in input_arr:
    while stack_arr and stack_arr[-1] == result: # stack_arr 가 비어있지 않고, stack_arr의 가장 위가 result랑 같은지 확인인
        stack_arr.pop() # stack 에서 값을 꺼낸다.
        result += 1 # 다음 숫자로 넘어감감

    if i == result: # 지금 숫자가 찾는 숫자면 다음 숫자로 목표 변경경
        result += 1
    else:
        stack_arr.append(i) # 아니니까 stack에 집어 넣음음

while stack_arr: # stack_arr가 비어있지 않다면 실행행
    if stack_arr[-1] == result: # 가장 위의 숫자가 찾는 숫자면
        stack_arr.pop() # pop으로 뽑아냄
        result += 1 # 다음 숫자로 넘어감감
    else:
        state = "Sad" # 다음 숫자가 stack의 가장 위에도, 입력 값에도 없다면 Sad로 상태 변경
        break

print(state)
