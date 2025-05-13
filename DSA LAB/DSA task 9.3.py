def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  #
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    for num in arr:
        count[num - min_val] += 1
    for i in range(1, range_of_elements):
        count[i] += count[i - 1]
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return output
def generate_random_list(size, max_value=10000):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, max_value))  #
    return arr
def measure_time(algorithm, arr):
    start_time = get_current_time()
    algorithm(arr)
    end_time = get_current_time()
    return end_time - start_time
def get_current_time():
    import time  
    return time.time()
def compare_algorithms():
    sizes = [1000, 5000, 10000]  
    heap_sort_times = []
    counting_sort_times = []

    for size in sizes:
        arr = generate_random_list(size)
        heap_sort_times.append(measure_time(heap_sort, arr.copy()))
        counting_sort_times.append(measure_time(counting_sort, arr.copy()))

    return sizes, heap_sort_times, counting_sort_times
def print_performance():
    sizes, heap_sort_times, counting_sort_times = compare_algorithms()

    print("Performance Comparison of Heap Sort and Counting Sort (in seconds):")
    print("List Size | Heap Sort | Counting Sort")
    print("--------------------------------------")
    for i in range(len(sizes)):
        print(f"{sizes[i]:9} | {heap_sort_times[i]:10.6f} | {counting_sort_times[i]:10.6f}")
print_performance()

