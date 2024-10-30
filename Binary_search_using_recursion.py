def binary_search_recursion(arr,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if arr[mid]==x:
        return mid+1
    elif arr[mid]>x:
        return binary_search_recursion(arr,x,si,mid-1)
    else:
        return  binary_search_recursion(arr,x,mid+1,ei)
        
        
x=4
si=0
jab=[1,2,3,4,6,10]
l=len(jab)
print(binary_search_recursion(jab,x,si,l-1))

        
