print("Hello this is Untold_mystery\n")

def num(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end=" ")
        print()
num(5)