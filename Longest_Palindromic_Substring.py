def palendrome_substring(s):
    n = len(s)
    s_string = ""
    for i in range(n):
        for j in range(i,n):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                if len(s_string)<len(substring):
                    s_string = substring
    return s_string

s = input("Enter the string: ")
print(palendrome_substring(s))