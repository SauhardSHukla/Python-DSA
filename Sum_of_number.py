# Print the sum of first N natural numbers

num=1
n=int(input())
s=0
while num<=n:
    if num %2==0:
        s+=num
    num+=1
print(s)
