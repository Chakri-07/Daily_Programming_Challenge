def longestSubstring(s: str) -> int:
    k = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in k:
            k.remove(s[left])
            left += 1
        k.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

print("Input a string:")
user_input = input()

result = longestSubstring(user_input)
print("Length of the longest substring without repeating characters:", result)