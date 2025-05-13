def exponential_search(arr, target):
    n = len(arr)
    if arr[0] == target:
        return 0  
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, i // 2, min(i, n - 1))
def binary_search(arr, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1 
def fibonacci_search(arr, target):
    n = len(arr)
    fib_m_2 = 0 
    fib_m_1 = 1  
    fib = fib_m_2 + fib_m_1  
    while fib < n:
        fib_m_2 = fib_m_1
        fib_m_1 = fib
        fib = fib_m_2 + fib_m_1
    offset = -1
    while fib > 1:
        i = min(offset + fib_m_2, n - 1)
        
        if arr[i] == target:
            return i
        elif arr[i] < target:
            fib = fib_m_1
            fib_m_1 = fib_m_2
            fib_m_2 = fib - fib_m_1
            offset = i
        else:
            fib = fib_m_2
            fib_m_1 -= fib_m_2
            fib_m_2 = fib - fib_m_1
    if fib_m_1 and arr[offset + 1] == target:
        return offset + 1
    
    return -1  
def generate_random_list(size, max_value=10000):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, max_value))  
    return arr
def measure_time(algorithm, arr, target):
    start_time = get_current_time()
    algorithm(arr, target)
    end_time = get_current_time()
    return end_time - start_time
def get_current_time():
    import time 
    return time.time()
def compare_algorithms():
    sizes = [1000, 5000, 10000]  
    binary_search_times = []
    exponential_search_times = []
    fibonacci_search_times = []

    for size in sizes:
        arr = generate_random_list(size)
        sorted_arr = sorted(arr)  
        target = arr[size // 2] 
        binary_search_times.append(measure_time(binary_search, sorted_arr, target, 0, size - 1))
        exponential_search_times.append(measure_time(exponential_search, sorted_arr, target))
        fibonacci_search_times.append(measure_time(fibonacci_search, sorted_arr, target))

    return sizes, binary_search_times, exponential_search_times, fibonacci_search_times
def print_performance():
    sizes, binary_search_times, exponential_search_times, fibonacci_search_times = compare_algorithms()

    print("Performance Comparison of Binary Search, Exponential Search, and Fibonacci Search (in seconds):")
    print("List Size | Binary Search | Exponential Search | Fibonacci Search")
    print---------------------------------------------------------------
    for i in range(len(sizes)):
        print(f"{sizes[i]:9} | {binary_search_times[i]:12.6f} | {exponential_search_times[i]:18.6f} | {fibonacci_search_times[i]:16.6f}")
print_performance()
