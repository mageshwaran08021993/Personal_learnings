# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K, L):
    # write your code in Python 3.8.10
    if len(A) < K+L:
        return -1
    def max_val(lt, n, l): # l =4, n=2, len(lt) - 7
        max_v=lt[0]
        for i in range(0, len(lt)-(n+l)+1):
          j=0
          while j < len(lt):
            # if lt[j:n] == lt[i:n]:
            # i = 1
            # j=0
            if j < i+n:
              j=j+n+i
            else:
              v=sum(lt[i:(i+n)]) + sum(lt[(j):(j+l)])
              # print(lt[i:(i+n)], lt[(j):(j+l)], v)
              if max_v < v:
                print(lt[i:(i+n)], lt[(j):(j+l)], v)
                max_v=v
              j+=1
        print("Max - ", max_v)
        return max_v
    return max(max_val(A, L, K), max_val(A, K, L))

# print(solution([4,3,5,5, 4], 3, 1))
print(solution([  8, 20, 23, 6, 3, 34, 6], 4, 2))

# i=1, n=4
# j=0, j+n = j = 5< i+l,