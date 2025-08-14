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
    
    if not t:
        return 0
    if t[0] == 1:
        return len(t)
    else:
        return len(t) - 1