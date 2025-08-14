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
    return len(t) if t and t[0] == 1 else max(0, len(t) - 1)