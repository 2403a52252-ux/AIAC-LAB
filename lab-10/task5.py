import time
# Original (slow) approach
start = time.time()
nums = [i for i in range(1, 1000000)]
squares = []
for n in nums:
    squares.append(n**2)
original_time = time.time() - start
print(f"Original: {len(squares)} squares in {original_time:.4f} seconds")

# Optimized with list comprehension
start = time.time()
squares = [i**2 for i in range(1, 1000000)]
list_comp_time = time.time() - start
print(f"List comprehension: {len(squares)} squares in {list_comp_time:.4f} seconds")

print(f"\nSpeedup: List comprehension is {original_time/list_comp_time:.1f}x faster")

