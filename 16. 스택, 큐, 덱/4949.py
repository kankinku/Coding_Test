while True:
    text = input()
    if text == ".":
        break

    check_stack = []
    balanced = True 

    for char in text:
        if char in "([":
            check_stack.append(char)
        elif char == ")":
            if check_stack and check_stack[-1] == "(":
                check_stack.pop()
            else:
                balanced = False
                break
        elif char == "]":
            if check_stack and check_stack[-1] == "[":
                check_stack.pop()
            else:
                balanced = False
                break

    if balanced and not check_stack:
        print("yes")
    else:
        print("no")
