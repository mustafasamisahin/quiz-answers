def jumping_on_clouds(c):
    jump_count = 0
    i = 0
    while (i < len(c)-1):
        if (i + 2 < len(c)):
            if (c[i + 2] == 0):
                i += 2
            else:
                i += 1
        else:
            i += 1
        jump_count += 1
    return jump_count
    