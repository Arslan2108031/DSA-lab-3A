def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def generate_random_list(size):
    return [int((i * 1234567) % 10000) for i in range(size)]
import time
random_list = generate_random_list(1000)
start_time = time.time()
bubble_sorted = bubble_sort(random_list.copy())
bubble_sort_time = time.time() - start_time
start_time = time.time()
merge_sorted = merge_sort(random_list.copy())
merge_sort_time = time.time() - start_time
start_time = time.time()
quick_sorted = quick_sort(random_list.copy())
quick_sort_time = time.time() - start_time
print(f"Bubble Sort Time: {bubble_sort_time:.5f} seconds")
print(f"Merge Sort Time: {merge_sort_time:.5f} seconds")
print(f"Quick Sort Time: {quick_sort_time:.5f} seconds")
print("\nTime Complexity Explanation:")
print("1. Bubble Sort: O(n²) in worst/average case.")
print("2. Merge Sort: O(n log n) in all cases.")
print("3. Quick Sort: O(n log n) on average, but can degrade to O(n²) in worst case.")

