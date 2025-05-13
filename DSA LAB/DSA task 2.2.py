def brute_force_longest_substring(s):
    max_len = 0
    longest = ""
    comparisons = 0  

    for i in range(len(s)):
        seen = ""
        for j in range(i, len(s)):
            comparisons += 1
            if s[j] in seen:
                break
            seen += s[j]
        if len(seen) > max_len:
            max_len = len(seen)
            longest = seen

    return longest, max_len, comparisons

def sliding_window_longest_substring(s):
    seen = {}
    start = 0
    max_len = 0
    longest = ""
    steps = 0

    for end in range(len(s)):
        char = s[end]
        steps += 1
        if char in seen and seen[char] >= start:
            start = seen[char] + 1  
        seen[char] = end
        if end - start + 1 > max_len:
            max_len = end - start + 1
            longest = s[start:end+1]

    return longest, max_len, steps

test_strings = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    "abcdefg",
    "abba",
    "",
    "a",
    "abcadefghijklmno",
]

print("=== Longest Substring Without Repeating Characters ===\n")

for s in test_strings:
    print(f"Input string: {s!r}")

    brute_result, brute_len, brute_steps = brute_force_longest_substring(s)
    slide_result, slide_len, slide_steps = sliding_window_longest_substring(s)

    print(f"[Brute Force]    → Substring: {brute_result!r}, Length: {brute_len}, Steps: {brute_steps}")
    print(f"[Sliding Window] → Substring: {slide_result!r}, Length: {slide_len}, Steps: {slide_steps}")
    print("----")
