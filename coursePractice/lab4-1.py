import math

class Color:
    def __init__(self):
        self.c = 0
        self.m = 0
        self.y = 0
        self.k = 0

def is_power_of_two(n):
    return (n > 0) and ((n & (n - 1)) == 0)

def access_cache(cache, index):
    if cache[index]:
        return True,  # Cache hit
    else:
        cache[index] = True 
        return False,  # Cache miss

def main():
    N = int(input("Enter N (power of 2): "))
    while not is_power_of_two(N):
        N = int(input("N must be a power of 2. Enter again: "))

    M = int(input("Enter M (power of 2): "))
    while not is_power_of_two(M):
        M = int(input("M must be a power of 2. Enter again: "))

    K = int(input("Enter K (power of 2, <= NxM/4): "))
    while not is_power_of_two(K) or K > (N * M) // 4:
        K = int(input("K must be a power of 2 and <= NxM/4. Enter again: "))

    # Create main memory
    memory = [[Color() for _ in range(M)] for _ in range(N)]

    # Cache implementation
    cache_size = K // 8  # Assuming sizeof(Color) is 8 bytes (adjust if needed)
    cache = [False] * cache_size

    # Algorithm 1
    total_accesses1 = 0
    cache_misses1 = 0
    for i in range(N):
        for j in range(M):
            index = (i * M + j) % cache_size
            is_hit,  = access_cache(cache, index)
            if not is_hit:
                cache_misses1 += 1
            total_accesses1 += 1

            # ... (Actual memory operations)
            memory[i][j].c = 0
            memory[i][j].m = 0
            memory[i][j].y = 1
            memory[i][j].k = 0

    # ... (Similarly implement and analyze Algorithm 2 and Algorithm 3)

    # Output Results
    print("\nAlgorithm 1:")
    print("Total Accesses:", total_accesses1)
    print("Cache Misses:", cache_misses1)
    print("Cache Hits:", total_accesses1 - cache_misses1)
    # ... (Calculate and output hit/miss rates)

    # ... (Output results for Algorithm 2 and Algorithm 3)

if __name__ == "__main__":
    main()