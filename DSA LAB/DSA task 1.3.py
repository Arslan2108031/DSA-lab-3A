def log(n):
    count = 0
    i = 1
    while i < n:
        i *= 2
        count += 1
    return count

def constant(n):
    return [1 for _ in range(n)]

def log_n(n):
    return [log(i + 1) for i in range(n)]

def linear(n):
    return [i for i in range(n)]

def n_log_n(n):
    return [i * log(i + 1) for i in range(n)]

def quadratic(n):
    return [i * i for i in range(n)]

def exponential(n):
    return [2 ** (i // 100) for i in range(n)]  

sample_points = [1, 10, 50, 100, 200, 500, 1000]

print(f"{'n':<6} {'O(1)':>6} {'O(log n)':>10} {'O(n)':>6} {'O(n log n)':>12} {'O(n^2)':>10} {'O(2^n)':>8}")
print("-" * 60)
for n in sample_points:
    o1 = 1
    olog = log(n)
    on = n
    onlog = n * log(n)
    on2 = n * n
    o2n = 2 ** (n // 100)  
    print(f"{n:<6} {o1:>6} {olog:>10} {on:>6} {onlog:>12} {on2:>10} {o2n:>8}")
