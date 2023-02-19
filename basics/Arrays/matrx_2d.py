input_val = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
max_val = []
# print("length - ", len(input_val))
for i in range(0, len(input_val)-2):
  for j in range(0, len(input_val)-2):
    sum = input_val[i][j] + input_val[i][j+1] + input_val[i][j+2] + input_val[i+1][j+1] + input_val[i+2][j+0] + input_val[i+2][j+1] + input_val[i+2][j+2]
    # print(sum)
    max_val.append(sum)

print("max_val - ", max(max_val))
