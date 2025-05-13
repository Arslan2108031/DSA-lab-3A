import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i 
    return -1  
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] > target:
            high = pos - 1
        else:
            low = pos + 1
            
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
    jump_search_times = []
    interpolation_search_times = []
    binary_search_times = []

    for size in sizes:
        arr = generate_random_list(size)
        sorted_arr = sorted(arr)  
        target = arr[size // 2] 
        binary_search_times.append(measure_time(binary_search, sorted_arr, target))
        jump_search_times.append(measure_time(jump_search, sorted_arr, target))
        interpolation_search_times.append(measure_time(interpolation_search, sorted_arr, target))

    return sizes, binary_search_times, jump_search_times, interpolation_search_times
def print_performance():
    sizes, binary_search_times, jump_search_times, interpolation_search_times = compare_algorithms()

    print("Performance Comparison of Binary Search, Jump Search, and Interpolation Search (in seconds):")
    print("List Size | Binary Search | Jump Search | Interpolation Search")
    print---------------------------------------------------------
    for i in range(len(sizes)):
        print(f"{sizes[i]:9} | {binary_search_times[i]:12.6f} | {jump_search_times[i]:12.6f} | {interpolation_search_times[i]:18.6f}")
print_performance()

