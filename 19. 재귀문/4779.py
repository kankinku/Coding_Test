def cantoa(n):
    if n == 0:
        return "-"
    
    prev = cantoa(n - 1)
    space = " " * (3**(n - 1))
    return prev + space + prev

while True:
    try:
        n = int(input())
        print(cantoa(n))
    except:
        break