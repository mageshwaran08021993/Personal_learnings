def getFrecuency(s):
    result = {}
    for char in s:
        result[char] = result[char] + 1 if char in result else 1
    for k, v in result.items():
        result[k] = v/2
    return result


def reverseShuffleMerge(s):
    frecuency = getFrecuency(s)
    inserted = dict(zip(frecuency.keys(), [0 for _ in frecuency.keys()]))
    discarded = frecuency.copy()
    result = [s[-1]]
    inserted[s[-1]] += 1
    for c in s[-2::-1]:
        if(inserted[c] < frecuency[c]): ## Should I insert more 'c'?
            while len(result) > 0:
                if result[-1] > c and discarded[result[-1]] - 1 >= 0:
                    removed = result.pop()
                    discarded[removed] -= 1
                    inserted[removed] -= 1
                else:
                    break
            result.append(c)
            inserted[c] += 1
        else:
            discarded[c] -= 1
    return "".join(result)

  # l = len(s)
  # used_lt = []
  # uunsed_lt = []
  # req_lt = []
  # dict={}
  # req_dict = {}
  # ## Used one's
  # for i in s:
  #   if i in dict.keys():
  #     dict[i] = dict[i]+1
  #   else:
  #     dict[i]=1
  
  # # Required one's
  # for i,j in dict.items():
  #   req_dict[i] = int(j/2)

  # i=len(s)-1
  # unique_keys = list(dict.keys())
  # unique_keys.sort()
  # # while i >=0:
  # #   print("i val - ", i)
    
  # #   i-= 1
  # for i in unique_keys:
  #   while req_dict[i]>0:
  #     req_dict[i] = req_dict[i]-1
  #     req_lt.append(i)
  
  # print("req_dict - ", req_dict)
  # print("req_lt - ", "".join(req_lt))
input = "abcdefgabcdefg"
print(reverseShuffleMerge(input))
