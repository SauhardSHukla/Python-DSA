arr=(1,1,2,2,2,1,4)
count=[0]*5
for num in arr:
    count[num]+=1
    print(count)






def sort012(arr, n):
    low = 0       # Pointer for 0s
    mid = 0       # Pointer for 1s
    high = n - 1  # Pointer for 2s

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid+=1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    
    return arr




n=12
arr=[0,2,0,0,0,1,2,0,1,3,1,2]
sort=sort012(arr,n)
print(sort)
