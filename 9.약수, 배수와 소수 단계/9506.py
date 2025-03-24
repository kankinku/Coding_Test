while True:
    A = int(input())
    div = []
    if A == -1:
        break
    for i in range(1,A+1):
        if A%i ==0 :
            if i != A:
                div.append(i)
    if sum(div) == A:
        print(f"{A} = {div[0]}",end="")
        for i in range(1,len(div)):
            print(f" + {div[i]}",end="")
        print("")
    else:
        print(f"{A} is NOT perfect.")