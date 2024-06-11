def lastSubstringBeforeEmpty(s: str) -> str:
    last_substring = ""
    char_indices = {chr(ord('a') + i): -1 for i in range(26)}
    
    while s:
        for char in char_indices:
            if char in s:
                char_index = s.index(char)
                last_substring += s[:char_index]
                s = s[char_index+1:]
                char_indices[char] = -1
                break
        else:
            break
    
    return last_substring

s = "aabcbbca"
print(lastSubstringBeforeEmpty(s))  # Output: "ba"

#Time complexity:O(n^2)
#Space complexity:O(1)
