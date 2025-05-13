def get_time():
    from time import perf_counter  
    return perf_counter()

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def test_fib_methods(n_values):
    print(f"{'n':<5} {'Recursive':>15} {'Iterative':>15} {'Memoized':>15}")
    print("-" * 50)
    
    for n in n_values:
       
        start = get_time()
        fib_recursive(n)
        time_recursive = get_time() - start
     
        start = get_time()
        fib_iterative(n)
        time_iterative = get_time() - start
       
        start = get_time()
        fib_memo(n, {})  
        time_memoized = get_time() - start
      
        print(f"{n:<5} {time_recursive:>15.6f} {time_iterative:>15.6f} {time_memoized:>15.6f}")

test_fib_methods([10, 20, 30, 40])
