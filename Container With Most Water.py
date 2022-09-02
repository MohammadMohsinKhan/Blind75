def mostWater(height):
    max = 0
    i = 0
    j = len(height) - 1
    
    while (i < j):
        area = ((j-i) * min(height[i], height[j]))
        if (area > max):
            max = area
        
        if (height[i] < height[j]):
            i += 1
        else:
            j -= 1

    return max

print(mostWater([1,8,6,2,5,4,8,3,7]))