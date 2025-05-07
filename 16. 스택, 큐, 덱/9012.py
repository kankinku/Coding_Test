N = int(input())
for _ in range(N):
    stack = []
    is_valid = True
    s = input()

    for char in s:
        if char == '(':
            stack.append('(')
        else:  
            if stack:
                stack.pop()
            else:
                is_valid = False
                break

    if is_valid and not stack:
        print("YES")
    else:
        print("NO")
