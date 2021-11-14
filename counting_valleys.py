def counting_valleys(steps, path):
    valley_count = 0
    location = 0
    for i in range(steps):
        if (location == 0 and path[i] == 'D'):
            valley_count += 1
        if (path[i] == 'U'):
            location += 1
        else:
            location -= 1
        
                
    return valley_count