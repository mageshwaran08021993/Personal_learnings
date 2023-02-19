# acct_num = "12345677"
# print("123456789"[0::1])

seq = "12345#12478"
  
# result contains odd numbers of the list
result = filter(None, [item.strip() for item in seq.split("#")])
print(list(result))

result = [item.strip() for item in seq.split("#")]
print(list(result))
