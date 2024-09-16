def reverse_string(s):
    words = s.split()
    words = words[::-1]
    s = " ".join(words)
    return s

s = input()
print(reverse_string(s))