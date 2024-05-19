import math

class Color:
    def __init__(self):
        self.c = 0
        self.m = 0
        self.y = 0
        self.k = 0

# Function to check if a number is a power of 2
def is_power_of_two(n):
    return (n > 0) and ((n & (n - 1)) == 0)

def access_cache(row, col, num_blocks, cache_size, cache_valid, cache_tag, hits, misses):
    block_index = (row * M + col) // num_blocks
    tag = row // (cache_size // N)

    if cache_valid[block_index] and cache_tag[block_index] == tag:
        return hits + 1, misses  # Return updated hits
    else:
        cache_valid[block_index] = True
        cache_tag[block_index] = tag
        return hits, misses + 1  # Return updated misses

# Get input from the user
N = int(input("Enter the dimension N (power of 2): "))
M = int(input("Enter the dimension M (power of 2): "))
K = int(input("Enter the cache block size K (power of 2, K <= NxM/4): "))

# Validate input
if not is_power_of_two(N) or not is_power_of_two(M) or not is_power_of_two(K) or K > (N * M) / 4:
    print("Invalid input. Please ensure N, M, and K are powers of 2, and K <= NxM/4.")
    exit()

# Create the main memory
memory = [[Color() for _ in range(M)] for _ in range(N)]

# Calculate cache parameters
num_blocks = K // 4  # 4 bytes per color
cache_size = N * M // num_blocks

# Simulate the cache (Direct Mapping)
cache_valid = [False] * cache_size
cache_tag = [0] * cache_size

# Run Algorithms and analyze cache performance
for algo in range(1, 4):
    total_accesses = 0
    hits = 0
    misses = 0

    print(f"\nAlgorithm {algo}:")

    if algo == 1:
        for i in range(N):
            for j in range(M):
                for _ in range(4):  # Access each color component
                    hits, misses = access_cache(i, j, num_blocks, cache_size, cache_valid, cache_tag, hits, misses)
                    total_accesses += 1
                memory[i][j].c = 0
                memory[i][j].m = 0
                memory[i][j].y = 1
                memory[i][j].k = 0

    # ... (rest of the code for algorithms 2 and 3 is the same) 

    print("Total Accesses:", total_accesses)
    print("Hits:", hits)
    print("Misses:", misses)
    print("Hit Rate: {:.2f}%".format(hits / total_accesses * 100))
    print("Miss Rate: {:.2f}%".format(misses / total_accesses * 100))