def rot_left(a, d):
    # Write your code here
    for i in range(d):
        a.append(a[0])
        a.pop(0)
    return a