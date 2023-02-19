input_val = [1, 2, 3, 4, 5]

d = 2
new_val = input_val[:]
ne=[]
for i in range(d, len(input_val)):
  ne.append(input_val[i])

for i in range(0, d):
  ne.append(input_val[i])
print(ne)