def luckBalance(k, contests):
    # Write your code here
    important_contest = []
    for arr in contests:
      if arr[1] == 1:
        important_contest.append(arr)
    print("Important contests - ", important_contest)

    sorted_arr = sorted(important_contest, key=lambda x:x[0], reverse=False)
    print("sorted_arr - ", sorted_arr)
    req_arr = sorted_arr[:len(sorted_arr)-k]
    print("required arr - ", req_arr)
    check = len(sorted_arr)-k
    sum = 0
    # for arr in contests:
    print("arr - ", arr)
    for arr in contests:
      if arr in req_arr and check > 0:
        sum-=arr[0]
        check-=1
      else:
        sum+=arr[0]
    # print("sum - ", sum)
    return sum

# def luckBalance(k, contests):
#     luck=0
#     important = []
#     for x in contests:
#         luck+=x[0]
#         if x[1]==1:
#             important.append(x[0])
#     important.sort()
#     if len(important)>k:
#         luck -= 2* sum(important[0:len(important)-k])
#     return luck
from datetime import datetime
start_time = datetime.now()    
k=5
contests = [[13, 1], [10, 1], [9, 1], [8, 1], [13, 1], [12, 1], [18, 1], [13, 1]]
print(luckBalance(k, contests))
end_time = datetime.now()
print(end_time-start_time)
# 0:00:00.000395, 0:00:00.000304, 0:00:00.000557, 0:00:00.000545