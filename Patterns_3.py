#Print the Numbers in Mirror form

n=int(input())
i=1
while i<=n:
    star=1
    while star<=n-i:
        print("*",end="")
        star+=1
    num=1
    while num<=i:
        print(num,end="")
        num+=1
    print()
    i+=1
    
    
