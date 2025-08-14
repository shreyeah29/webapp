def maximizeScore(arr):
    from bisect import bisect_left
    t = []
    for i, v in enumerate(arr, 1):
        if v <= i:
            j = bisect_left(t, v)
            if j == len(t):
                t.append(v)
            else:
                t[j] = v
    
    result = len(t)
    if len(t) > 2 and t and t[0] > 1:
        result -= 1
    
    return result