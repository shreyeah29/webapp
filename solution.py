def solve(N, A):
    events = []
    
    for arrival, departure, dishes in A:
        events.append((arrival, dishes))
        events.append((departure + 1, -dishes))
    
    events.sort()
    
    max_chefs = 0
    current_dishes = 0
    
    for time, change in events:
        current_dishes += change
        max_chefs = max(max_chefs, current_dishes)
    
    return max_chefs