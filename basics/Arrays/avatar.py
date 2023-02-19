import sys
import math
from contextlib import redirect_stdout


def compute_final_position(width, height, position, portal_a, portal_b, moves):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    c_h = position[1]
    c_w = position[0]
    current_position=position
    for m in moves:
      if m.upper() == 'U':
          if c_h < height-1 and c_h-1 in portal_a:
            c_h=portal_a[1]
            c_w=portal_a[0]
          elif c_h < height-1 and c_h-1 in portal_b:
            c_h=portal_b[1]
            c_w=portal_b[0]
          else:
            c_h-=1
      if m.upper() == 'D':
          if c_h < height-1 and c_h+1 in portal_a:
            c_h=portal_a[1]
            c_w=portal_a[0]
          elif c_h < height-1 and c_h+1 in portal_b:
            c_h=portal_b[1]
            c_w=portal_b[0]
          else:
            c_h+=1
      if m.upper() == 'R':
          if c_w < width-1 and c_h+1 in portal_a:
            c_h=portal_a[1]
            c_w=portal_a[0]
          elif c_w < width-1 and c_h+1 in portal_b:
            c_h=portal_b[1]
            c_w=portal_b[0]
          else:
            c_w+=1
      if m.upper() == 'L':
          if c_w < width-1 and c_h-1 in portal_a:
            c_h=portal_a[1]
            c_w=portal_a[0]
          elif c_w < width-1 and c_h-1 in portal_b:
            c_h=portal_b[1]
            c_w=portal_b[0]
          else:
            c_w-=1
      
    return c_w,c_h


      # for h in range(c_h, height):
      #     for w in range(c_w, width):
          



# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    width = 5
    height = 4
    moves = "RL"
    position = [3,0]
    portal_a = [1,1]
    portal_b = [2,3]
    print(compute_final_position(width, height, position, portal_a, portal_b, moves))

if __name__ == "__main__":
    main()
# Ignore and do not change the code above
