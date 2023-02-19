
from math import ceil


student_marks = {"a": [12, 16, 26],
                  "b": [45, 23, 12]}
query_name = "a"
marks = student_marks.get(query_name)
average = format(sum(marks)/len(marks), '.2f')
print(average)

