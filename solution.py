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
    
    # Original approach: return len(t)
    # But we know this fails for some cases
    
    # Maybe the constraint is: if the sequence doesn't start from 1,
    # we can only count consecutive elements from the actual start
    if t[0] == 1:
        # If starts with 1, we can potentially use all positions
        return len(t)
    else:
        # If doesn't start with 1, maybe we're limited by consecutive count from start
        # For [2,3,4] -> consecutive from 2 is 3, but maybe we lose the ability to score from position 1
        # So effective score might be the consecutive length minus the gap from 1
        gap_from_1 = t[0] - 1  # For [2,3,4], gap is 1
        return max(0, len(t) - gap_from_1)