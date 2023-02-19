# def minimumAbsoluteDifference(arr):
#     # Write your code here
#   diff = []
#   for i in range(0, len(arr)):
#     for j in range(i, len(arr)-1):
#       print(f"arr[j] - {arr[i]} and arr[j+1] - {arr[j+1]}")
#       diff.append(abs(arr[i] - arr[j+1])) 
#   return min(diff)

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort() 
    minimum = abs(arr[0] - arr[-1]) 

    for i in range(1, len(arr)): 
        diff = abs(arr[i - 1] - arr[i])
        if diff < minimum: 
            minimum = diff
    
    return minimum

arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
print(minimumAbsoluteDifference(arr=arr))