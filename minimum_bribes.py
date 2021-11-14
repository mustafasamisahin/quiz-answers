def minimum_bribes(q):
    count = 0
    q = [p-1 for p in q]
    for i in range(len(q)):
        if (q[i] - i) > 2:
            print("Too chaotic")
            return
        for j in range(max(q[i]-1,0), i):
            if q[j] > q[i]:
                count += 1
        
    print(count)