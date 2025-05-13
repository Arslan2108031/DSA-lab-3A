def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True

def test_are_anagrams():
    print(are_anagrams("listen", "silent"))  
    print(are_anagrams("hello", "world"))   
    print(are_anagrams("evil", "vile"))     
    print(are_anagrams("restful", "fluster"))
    print(are_anagrams("aabbcc", "abcabc"))   
    print(are_anagrams("aabbc", "abbcc"))     
    print(are_anagrams("", ""))              
    print(are_anagrams("a"*1000 + "b"*1000, "b"*1000 + "a"*1000))  

if __name__ == "__main__":
    test_are_anagrams()
