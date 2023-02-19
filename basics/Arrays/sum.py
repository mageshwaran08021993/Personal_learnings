# def compute_multiples_sum(n):
#     # Write your code here
#     # To debug: print("Debug messages...", file=sys.stderr, flush=True)
#     # return -1
#     sum=0
#     for i in range(1, n):
#         print(i)
#         if i%3 == 0 or i%5 ==0 or i%7 ==0:
#           print("inside if - ", i)
#           sum+=i
#     if sum == 0:
#       return -1
#     return sum

# print(compute_multiples_sum(1))


def find_smallest_interval(numbers):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    sort_val = sorted(numbers)
    print("sorted_val - ", sort_val)
    smallest = sort_val[0]
    for i in range(1, len(sort_val)):
        if smallest > (sort_val[i] - sort_val[i-1]):
            smallest= sort_val[i] - sort_val[i-1]
    return smallest
print(find_smallest_interval([1,6,4,8,2]))