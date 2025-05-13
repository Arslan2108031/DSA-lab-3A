def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True
        if not swapped:
            break
    return arr
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    return arr
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
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
    sizes = [100, 200, 300, 400, 500]  
    bubble_times = []
    selection_times = []
    insertion_times = []

    for size in sizes:
        arr = generate_random_list(size)
        bubble_times.append(measure_time(bubble_sort, arr.copy()))
        selection_times.append(measure_time(selection_sort, arr.copy()))
        insertion_times.append(measure_time(insertion_sort, arr.copy()))

    return sizes, bubble_times, selection_times, insertion_times
def print_performance():
    sizes, bubble_times, selection_times, insertion_times = compare_algorithms()

    print("Performance Comparison of Sorting Algorithms (in seconds):")
    print("List Size | Bubble Sort | Selection Sort | Insertion Sort")
    print("--------------------------------------------------------")
    for i in range(len(sizes)):
        print(f"{sizes[i]:9} | {bubble_times[i]:12.6f} | {selection_times[i]:14.6f} | {insertion_times[i]:14.6f}")
print_performance()

