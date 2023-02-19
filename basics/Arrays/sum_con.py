def compute_check_digit(identification_number):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # return -1
    even_sum=0
    odd_sum = 0
    str_val = str(identification_number)
    for i in range(0, len(str_val)):
        if i%2 == 0:
            even_sum+=int(str_val[i])
        else:
            odd_sum+=int(str_val[i])
    
    mul_res= (even_sum*3) + (odd_sum)
    last_d = int(str(mul_res)[-1])
    sub_v=0
    if last_d !=0:
        sub_v= 10 - last_d
    return sub_v

print(compute_check_digit(398471231234))