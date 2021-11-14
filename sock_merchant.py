def sock_merchant(n, ar):
    values = dict()
    pair_count = 0
    for i in range(n):
        if ar[i] in values:
            values[ar[i]] += 1
        else:
            values[ar[i]] = 1
    print (values)
    
    for key, value in values.items():
        if (value > 1):
            pair_count += value // 2
    return pair_count