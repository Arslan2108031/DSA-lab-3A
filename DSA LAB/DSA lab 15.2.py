def permute(s):
    results = []
    chars = list(s)
    n = len(chars)

    def backtrack(start):
        if start == n:
            results.append("".join(chars))
            return
        for i in range(start, n):
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1)
            chars[start], chars[i] = chars[i], chars[start]

    backtrack(0)
    return results
input_str = "ABC"
permutations = permute(input_str)

print("All permutations of", input_str, "are:")
for p in permutations:
    print(p)
print("\nTime Complexity:")
print("- O(N!) where N is the length of the string.")
print("- Each level of recursion fixes one character and permutes the rest.")
print("\nUse Cases:")
print("1. Password Generation: Generating all possible password combinations for a given set of characters.")
print("2. Anagrams: Finding all anagrams of a given word.")
print("3. Puzzles: Generating possible configurations of pieces.")
