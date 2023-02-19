#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = "7 3".split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = ["Tsi", r"h%x", "i #", "sM ", "$a ", "#t%", "ir!"]

format_str=""
for i in range(0, m):
  for val in matrix:
    format_str +=  val[i]
# print(re.sub('[!@#$%&]{2}', ' ', format_str))

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
print(re.search( r'(?<=\w)[\W]+(?=\w)', format_str).group())
