def hourglass_sum(arr):
    # Write your code here
    x = 0
    y = 0
    sums = []
    while (x < 4):
        while (y < 4):
            total = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            sums.append(total)
            y += 1
        x += 1
        y = 0
    return max(sums)
        
        
    