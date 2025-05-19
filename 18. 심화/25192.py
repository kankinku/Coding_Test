N = int(input())
total = 0
user_set = set()

for _ in range(N):
    command = input()
    if command == "ENTER":
        user_set.clear() 
    else:
        if command not in user_set:
            total += 1
            user_set.add(command)

print(total)
