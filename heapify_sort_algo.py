def swap(arr,idx1,idx2):
    arr[idx1],arr[idx2] = arr[idx2],arr[idx1]

def heapify(arr,n,pos):
    idx=pos
    while 2*idx <= n:
        large  = idx
        left = 2*idx
        right= 2*idx+1
        if arr[large] < arr[left]:
            large = left
        
        if right<= n and arr[large]< arr[right]:
            large= right
        
        if large == idx:
            break

        swap(arr,large,idx)
        idx=large 


if __name__ == "__main__":

    arr=[0,1,2,3,4,5,6]
    n=6

    for x in range(n,0,-1):
        heapify(arr,n,x)
    print("Max heap :"+str(arr))
    
    for x in range(n,0,-1):
        swap(arr,1,x)
        heapify(arr,x-1,1)
    print("Sorted heap :"+str(arr))