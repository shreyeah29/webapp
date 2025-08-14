def maximizeScore(arr):
    s, m = set(arr), 0
    for x in s:
        if x - 1 not in s:
            c = 0
            while x in s: c, x = c + 1, x + 1
            m = max(m, c)
    return m