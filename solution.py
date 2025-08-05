def solve(N, A):
    from collections import defaultdict
    
    load = defaultdict(int)
    
    for arrival, departure, dishes in A:
        for _ in range(dishes):
            min_load = min(load[t] for t in range(arrival, departure + 1))
            best_time = next(t for t in range(arrival, departure + 1) if load[t] == min_load)
            load[best_time] += 1
    
    return max(load.values()) if load else 0