def fib_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]
def fib_tabulation(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
n = 10
result_memo = fib_memoization(n)
result_tab = fib_tabulation(n)

print("Fibonacci using Memoization (n =", n, "):", result_memo)
print("Fibonacci using Tabulation  (n =", n, "):", result_tab)
print("\nEfficiency Comparison:")
print("- Memoization stores previously computed values in a dictionary.")
print("- Tabulation builds the solution from the bottom up using an array.")
print("- Both reduce time complexity from O(2^n) to O(n).")
