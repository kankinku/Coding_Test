def make_star(n):
    if n == 1:
        return ["*"]
    
    prev = make_star(n // 3)
    result = []

    for line in prev:
        result.append(line * 3)
    for line in prev:
        result.append(line + " " * (n // 3) + line)
    for line in prev:
        result.append(line * 3)

    return result

n = int(input()) 
stars = make_star(n)
for line in stars:
    print(line)
