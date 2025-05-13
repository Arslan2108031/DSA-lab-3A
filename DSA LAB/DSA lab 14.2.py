def lcs_memo(s1, s2):
    memo = {}

    def helper(i, j):
        key = (i, j)
        if key in memo:
            return memo[key]
        if i == len(s1) or j == len(s2):
            return ""
        if s1[i] == s2[j]:
            memo[key] = s1[i] + helper(i + 1, j + 1)
        else:
            option1 = helper(i + 1, j)
            option2 = helper(i, j + 1)
            memo[key] = option1 if len(option1) > len(option2) else option2
        return memo[key]

    return helper(0, 0)
def lcs_tab(s1, s2):
    m, n = len(s1), len(s2)
    table = [["" for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                table[i + 1][j + 1] = table[i][j] + s1[i]
            else:
                if len(table[i + 1][j]) > len(table[i][j + 1]):
                    table[i + 1][j + 1] = table[i + 1][j]
                else:
                    table[i + 1][j + 1] = table[i][j + 1]

    return table[m][n]
s1 = "AGGTAB"
s2 = "GXTXAYB"

print("LCS using Memoization:", lcs_memo(s1, s2))   
print("LCS using Tabulation :", lcs_tab(s1, s2))  
print("\nTime Complexity:")
print("- Memoization: O(m*n) with recursion and cache")
print("- Tabulation : O(m*n) with 2D table")
