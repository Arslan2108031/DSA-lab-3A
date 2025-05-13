def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def generate_random_list(size):
    arr = []
    for i in range(size):
        arr.append(size * 10 - i)
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
    quick_sort_times = []
    merge_sort_times = []

    for size in sizes:
        arr = generate_random_list(size)
        quick_sort_times.append(measure_time(quick_sort, arr.copy()))
        merge_sort_times.append(measure_time(merge_sort, arr.copy()))

    return sizes, quick_sort_times, merge_sort_timesn
def print_performance():
    sizes, quick_sort_times, merge_sort_times = compare_algorithms()

    print("Performance Comparison of Quick Sort and Merge Sort (in seconds):")
    print("List Size | Quick Sort | Merge Sort")
    print("--------------------------------------")
    for i in range(len(sizes)):
        print(f"{sizes[i]:9} | {quick_sort_times[i]:10.6f} | {merge_sort_times[i]:10.6f}")
print_performance()
