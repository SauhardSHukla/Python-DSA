##def First_Index(arr,x):
##    if not arr:
##        return -1
##    if arr[0]==x:
##        return 0
##    index=First_Index(arr[1:],x)
##    if index!=-1:
##        return index+1
##    return -1
##arr=[1,2,3,43,24,2]
##x=24
##sort=First_Index(arr,x)
##print(sort)


##def last_Index(arr,x):
##    l=len(arr)
##    if l==0:
##        return-1
##    a=arr[1:]
##    sml=last_Index(a,x)
##    if sml !=-1:
##        return sml+1
##    else:
##        if arr[0]==x:
##            return 0
##        return -1
##arr=[1,24,3,43,24,2]
##x=24
##sort=last_Index(arr,x)
##print(sort)

##def last_index_si(arr,x,si):
##    l=len(arr)
##    if (si== l):
##        return -1
##    sml=last_index_si(arr,x,si+1)
##    if sml!=-1:
##        return sml
##    else:
##        if arr[si]==x:
##            return si
##        return -1
##arr=[1,24,3,43,24,2]
##x=24
##si=0
##sort=last_index_si(arr,x,si)
##print(sort)












