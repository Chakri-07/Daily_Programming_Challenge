def is_valid_paranthesis(s):
    bracket = {"(":")","{":"}","[":"]"}
    stack = []
    k = False
    for char in s:
        if char in bracket:
            stack.append(char)
        if char in bracket.values():
            if (bracket[stack[-1]] == char):
                stack.pop()
            else:
                return k
    k = True
    return k

s = input("Enter the string: ")
print(is_valid_paranthesis(s))