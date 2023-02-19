def compute_closest_to_zero(ts):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if len(ts) == 0:
      return 0
    ts.sort()
    negative_lt = [i for i in ts if i < 0]
    positive_lt = [i for i in ts if i>0]
    if len(positive_lt) == 0:
      return negative_lt[-1]
    if len(negative_lt) == 0:
      return positive_lt[0]
    negative_low = negative_lt[-1]
    
    positive_low = positive_lt[0]
    if abs(negative_low) < abs(positive_low):
      return negative_low
    return positive_low

print(compute_closest_to_zero([15, 7, 9, 14, 12]))