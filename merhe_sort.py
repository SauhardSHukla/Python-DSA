##Merge Sort

def mergesort(arr,a1,a2):
    i=0
    j=0
    k=0
    while i <len(a1) and j<len(a2):
        if (a1[i]<=a2[j]):
            a[k]=a1[i]
            k+=1
            i+=1
            
        else:
            a[k]=a2[j]
            k=k+1
            j=j+1
    while i<len(a1):
        a[k]=a1[i]
        i+=1
        k+=1
    while j<len(a2):
        a[k]=a2[j]
        j+=1
        k+=1        

def sort(arr):
    if len(arr)
    mid=len(arr)//2
    a1=a[0:mid]
    a2=a[mid:]

    if len(a1)<=1 or len(a2)<=1:
        return
    sort(a1)
    sort(a2)

    mergesort(arr,a1,a2)
a=[2,3,42,3,4,2,3,32]
sort(a)
    
    
    
  
