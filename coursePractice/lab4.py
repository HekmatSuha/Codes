class Color:
    def __init__(self, c=0, m=0, y=0, k=0):
        self.c = c
        self.m = m
        self.y = y
        self.k = k

class Cache:
    def __init__(self, block_size, num_blocks):
        self.block_size = block_size
        self.num_blocks = num_blocks
        self.cache = [-1] * num_blocks

    def access(self, index):
        block_index = index // self.block_size
        cache_index = block_index % self.num_blocks

        hit = self.cache[cache_index] == block_index
        self.cache[cache_index] = block_index

        return hit

def simulate_algorithm(memory, cache, algorithm):
    N = len(memory)
    M = len(memory[0])

    total_accesses = 0
    hits = 0

    if algorithm == 1:
        for i in range(N):
            for j in range(M):
                total_accesses += 1
                if cache.access(i * M + j):
                    hits += 1
                memory[i][j].c = 0
                memory[i][j].m = 0
                memory[i][j].y = 1
                memory[i][j].k = 0
    elif algorithm == 2:
        for i in range(N):
            for j in range(M):
                total_accesses += 1
                if cache.access(j * N + i):
                    hits += 1
                memory[j][i].c = 0
                memory[j][i].m = 0
                memory[j][i].y = 1
                memory[j][i].k = 0
    elif algorithm == 3:
        for i in range(N):
            for j in range(M):
                total_accesses += 1
                if cache.access(i * M + j):
                    hits += 1
                memory[i][j].y = 1
        for i in range(N):
            for j in range(M):
                total_accesses += 1
                if cache.access(i * M + j):
                    hits += 1
                memory[i][j].c = 0
                memory[i][j].m = 0
                memory[i][j].k = 0

    misses = total_accesses - hits
    hit_rate = hits / total_accesses if total_accesses > 0 else 0
    miss_rate = misses / total_accesses if total_accesses > 0 else 0

    return total_accesses, hits, misses, hit_rate, miss_rate

def main():
    try:
        N = int(input("Enter N (power of 2): "))
        M = int(input("Enter M (power of 2): "))
        K = int(input("Enter cache block size (power of 2 and <= NxM / 4): "))

        if not (N & (N - 1) == 0 and N > 0):
            raise ValueError("N is not a power of 2")
        if not (M & (M - 1) == 0 and M > 0):
            raise ValueError("M is not a power of 2")
        if not (K & (K - 1) == 0 and K > 0):
            raise ValueError("K is not a power of 2")
        if not (K <= (N * M) // 4):
            raise ValueError("K should be <= NxM / 4")

        memory = [[Color() for _ in range(M)] for _ in range(N)]
        cache = Cache(block_size=K, num_blocks=(N * M) // (4 * K))

        for algorithm in range(1, 4):
            total_accesses, hits, misses, hit_rate, miss_rate = simulate_algorithm(memory, cache, algorithm)
            print(f"Algorithm {algorithm}:")
            print(f"Total Accesses: {total_accesses}")
            print(f"Hits: {hits}")
            print(f"Misses: {misses}")
            print(f"Hit Rate: {hit_rate:.2f}")
            print(f"Miss Rate: {miss_rate:.2f}")
            print()

    except ValueError as ve:
        print(f"Input error: {ve}")

if __name__ == "__main__":
    main()
