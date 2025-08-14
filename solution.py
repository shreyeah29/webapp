def processScheduling(n_intervals, n_processes):
    MOD = 10**9 + 7
    
    if n_intervals == 1:
        return n_processes % MOD
    
    if n_processes == 1:
        return 0
    
    return (n_processes * pow(n_processes - 1, n_intervals - 1, MOD)) % MOD

# For HackerRank format
if __name__ == "__main__":
    n_intervals = int(input())
    n_processes = int(input())
    print(processScheduling(n_intervals, n_processes))