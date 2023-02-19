if __name__ == '__main__':
    n = 5
    record = [["Rachel", -50], ["Mawer", -50], ["Sheen", -50], ["Shaheen", 51]]
    first = 0
    name_list = []
    lowest = record[0][1]
    largest2 = None
    lowest2 = None
    for val in record:
      print(val)
      if val[1] < lowest:
        lowest2 = lowest
        lowest = val[1]
      elif (lowest2 is None or lowest2 > val[1]) and lowest != val[1]:
        lowest2 = val[1]
    print("printing the target")
    name_lt =[]
    for i in record:
      if lowest2 in i:
        name_lt.append(i[0])
    name_lt.sort()
    print(name_lt)

