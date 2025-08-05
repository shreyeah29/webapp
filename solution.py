def solve(N, A):
    events = []
    
    # For each customer, distribute their dishes optimally across their time window
    for arrival, departure, dishes in A:
        time_window = departure - arrival + 1
        
        if dishes <= time_window:
            # Can spread dishes across different time slots (1 dish per slot)
            for i in range(dishes):
                t = arrival + i
                events.append((t, 1))
                events.append((t + 1, -1))
        else:
            # More dishes than time slots, need multiple dishes per slot
            base_dishes_per_slot = dishes // time_window
            extra_dishes = dishes % time_window
            
            for i in range(time_window):
                t = arrival + i
                dishes_at_t = base_dishes_per_slot + (1 if i < extra_dishes else 0)
                events.append((t, dishes_at_t))
                events.append((t + 1, -dishes_at_t))
    
    # Process events to find maximum concurrent dishes
    events.sort()
    max_concurrent = 0
    current_concurrent = 0
    
    for time, delta in events:
        current_concurrent += delta
        max_concurrent = max(max_concurrent, current_concurrent)
    
    return max_concurrent