#Patterns

n=int(input())
i=1
while i<=n:
    p=1
    while p<=n-i:
        print("*",end="")
        p+=1
    j=1
    while j<=i:
        print(n,end="")
        j+=1
    print()
    i+=1

