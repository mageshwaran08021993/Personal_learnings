# from collections import counter

from audioop import reverse


def programmerStrings(s):
    # Write your code here
    def find_program_index(s):
      a="programmer"
      a_dict = {"p":1,
                "r":3,
                "o":1,
                "g":1,
                "a":1,
                "m":2,
                "e":1
                }
      a=0
      index_1=0
      for i in range(0, len(s)):
        # print("i val - ", i)
        # print("i - ",i , s[i])
        if s[i] in a_dict.keys() and a_dict[s[i]] > 0:
          # print("key available")
          a_dict[s[i]] -= 1
        
        for j in a_dict.values():
          # print("dict val = ", j)
          if j != 0:
            a=1
            break
          a=0
        if a == 0:
          index_1 = i
          break
      return index_1
    
    first_index = find_program_index(s)
    print("index i - ", first_index+1)
    s_reverse = s[::-1]
    print("string re - ", s_reverse)
    second_index = find_program_index(s_reverse)
    print("second index - ", second_index+1)
    print("total_length - ", len(s)-(first_index+second_index+2))

if __name__ == '__main__':
  programmerStrings("proxgrammerxxprogrammer")