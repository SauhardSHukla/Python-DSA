
#Star Pattern
n=int(input())
i=1
while i<=n:
    spaces =1
    while spaces<=n-i:
        print(" ",end="")
        spaces+=1
    star1=1
    while star1<=i:
        print("*",end="")
        star1+=1
    star2=i-1
    while star2>=1:
        print("*",end="")
        star2-=1
    print()
    i+=1

#Pattern:triangle OF Numbers

j=int(input())
i=0

while i<=j:
    spaces =1
    while spaces <=j-i:
        print(" ",end="")
        spaces+=1
    num=1
    k=i
    while num<=i:
        print(k,end="")
        k+=1
        num+=1
    num2=1
    k-=2
    while num2 <i:
        print(k,end="")
        k-=1
        num2+=1
    print()
    i+=1




#Diamond Star
p=int(input())
half=n//2

i=0
while i<=half:
    spaces=half-i
    while spaces >0:
        print(" ",end="")
        spaces-=1
    star = 2*i+1
    while star>0:
        print("*",end="")
        star-=1
    print()
    i+=1
i=half-1
while i>=0:
    spaces =half-i
    while spaces >0:
        print(" ",end="")
        spaces-=1
    stars=2*i+1
    while stars>0:
        print("*",end="")
        stars-=1
    print()
    i-=1
        




















    
        
