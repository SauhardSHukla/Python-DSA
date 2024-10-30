n=int(input())
i=1

while i<=n:
    
    
    j=1
    while j<=i:
        print(i,end="")
        j+=1
        
    print()
    
    i+=1

#Print the reverse patterns

x=int(input())
i=1
while i<=n:
    j=1
    p=i
    while j<=i:
        print(p,end="")
        p-=1
        j+=1
    print()
    i+=1

#print inverted Numbers

a=int(input())
i=a
while i>0:
    j=1
    while j<=i:
        print(i,end="")
        j+=1
    print()
    i-=1
