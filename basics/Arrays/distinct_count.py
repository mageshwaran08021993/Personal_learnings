t= ["bcdef", "abcdefg", "bcde", "bcdef"]
# distinct_val = set(t)
# len_distinct = len(distinct_val)
# d=[]
# test={}
# for i in t:
#     if test.get(i,0) != 0:
#       continue
#     test[i]=1
#     counter = 0
#     for j in t:
#         if str(i) == str(j):
#             counter +=1
#     d.append([i, counter])
# print(len_distinct)
# [print(i[1], end=" ") for i in d]


# Optimized solution
from collections import Counter

s = set(t)
print(len(s))
d =  Counter(t)
for i in d.values():
    print(i, end = ' ')