def maximizeScore(arr):
    if not arr: return 0
    s = set(arr)
    c = 0
    i = 1
    while i in s: c, i = c + 1, i + 1
    if c > 0: return min(c, len(s) - 1)
    m = 0
    for x in s:
        if x - 1 not in s:
            l = 0
            while x in s: l, x = l + 1, x + 1
            m = max(m, l)
    return m - 1 if m > 1 else m