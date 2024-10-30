
#Continue

num=1
while num<=10:
    if num%2!=0:
        num+=1
        continue
    print (num)
    num+=1

#Break

num=10
while num <=30:
    if num==20:
        break
    print(num,)
    num+=2


num=10
while num <=30:
    if num==20:
        pass
        print("here is the number 20,")
       
    print(num,end=",")
    num+=2
