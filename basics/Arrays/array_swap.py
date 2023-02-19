def minimumSwaps(arr):
    swaps = 0
    l = len(arr)
    for slow in range(l):
        while arr[slow] != slow + 1:
            temp = arr[slow]-1
            arr[slow],arr[temp] = arr[temp],arr[slow]
            swaps += 1
    return swaps
    
arr = [4, 3, 1, 2]    
print(minimumSwaps(arr))