def minimumBribes(q):
    # Write your code here
    initial_que = [i for i in range(1, len(q)+1)]
    bribe=0
    for i in range(0, len(q)):
        if initial_que[i] == q[i]:
            pass
        elif initial_que[i+1] == q[i]:
            initial_que[i], initial_que[i+1] = initial_que[i+1], initial_que[i]
            bribe += 1
        elif initial_que[i+2] == q[i]:
            initial_que[i+1], initial_que[i+2] = initial_que[i+2], initial_que[i+1]
            initial_que[i], initial_que[i+1] = initial_que[i+1], initial_que[i]
            bribe +=2
        else:
            print("Too chaotic")
            return
    print(bribe)
    return

q = [1,2, 5, 3, 4, 7, 8, 6]
minimumBribes(q)