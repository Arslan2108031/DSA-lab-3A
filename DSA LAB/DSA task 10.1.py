def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  #
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1  #
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
    linear_search_times = []
    binary_search_times = []

    for size in sizes:
        arr = generate_random_list(size)
        sorted_arr = sorted(arr)
        target = arr[size // 2]  
        linear_search_times.append(measure_time(linear_search, arr, target))
        binary_search_times.append(measure_time(binary_search, sorted_arr, target))

    return sizes, linear_search_times, binary_search_times
def print_performance():
    sizes, linear_search_times, binary_search_times = compare_algorithms()

    print("Performance Comparison of Linear Search and Binary Search (in seconds):")
    print("List Size | Linear Search | Binary Search")
    print("--------------------------------------------")
    for i in range(len(sizes)):
        print(f"{sizes[i]:9} | {linear_search_times[i]:12.6f} | {binary_search_times[i]:12.6f}")
print_performance()
