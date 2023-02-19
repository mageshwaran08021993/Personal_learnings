# n val -  5
# queries -  [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

# def arrayManipulation(n, queries):
#   arr = [0 for i in range(1, n+1)]
#   for val in queries:  
#     for i in range(0, n+1):
#       if i >= val[0] and i <= val[1]:
#         arr[i-1]+=val[2]
#     print("eah i - ", arr)
#   print(max(arr))

def arrayManipulation(n, queries):
    arr = [0 for _ in range(n)]
    
    for a,b,k in queries:
        arr[a-1] +=k
        if b!=n:
            arr[b] -=k
        print("arr - ", arr)
    for i in range(1,n):
        arr[i]+=arr[i-1] 
    
    return max(arr)

n=5
queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
arrayManipulation(n, queries)